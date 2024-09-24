import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from torch.utils.tensorboard import SummaryWriter


# 1. 生成模拟数据集
def generate_data(num_samples):
    # 随机生成商品的价格和评分
    prices = np.random.uniform(1.0, 10.0, size=(num_samples, 1))  # 商品价格范围为 1.0 到 10.0
    ratings = np.random.uniform(1.0, 5.0, size=(num_samples, 1))  # 商品评分范围为 1.0 到 5.0

    # 标签: 假设价格 + 评分 > 10 的商品被认为是 "受欢迎"（标签为 1），否则为 "不受欢迎"（标签为 0）
    labels = (prices + ratings > 10).astype(int).reshape(-1)

    # 将数据转换为 PyTorch 张量
    X = torch.tensor(np.hstack((prices, ratings)), dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.long)

    return X, y


# 2. 定义简单的神经网络模型
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(2, 32)  # 输入层: 2 个特征（价格和评分），32 个神经元
        self.fc2 = nn.Linear(32, 2)  # 输出层: 2 个类别（受欢迎或不受欢迎）

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)  # 输出原始分数，不需要 softmax
        return x


# 3. 训练函数
def train(model, train_loader, test_loader, criterion, optimizer, device, writer):
    model.train()  # 切换到训练模式
    for epoch in range(10):  # 训练 20 个 epoch
        total_loss = 0
        for i, (data, labels) in enumerate(train_loader):
            data, labels = data.to(device), labels.to(device)

            optimizer.zero_grad()  # 梯度清零
            outputs = model(data)  # 前向传播
            loss = criterion(outputs, labels)  # 计算损失
            loss.backward()  # 反向传播
            optimizer.step()  # 更新权重
            total_loss += loss.item()  # 累加损失
            # 将损失记录到 TensorBoard
            writer.add_scalar('Loss/train', loss.item(), epoch * len(train_loader) + i)

        average_loss = total_loss / len(train_loader)
        # 测试模型并输出准确率
        accuracy = test(model, test_loader, device, writer, epoch)
        print(f'Epoch [{epoch + 1}/10], Average Loss: {average_loss:.4f}, Accuracy: {accuracy:.2f}%')

# 4. 测试函数
def test(model, test_loader, device, writer, epoch):
    model.eval()  # 切换到评估模式
    correct = 0
    total = 0
    with torch.no_grad():  # 不计算梯度
        for data, labels in test_loader:
            data, labels = data.to(device), labels.to(device)
            outputs = model(data)
            _, predicted = torch.max(outputs, 1)  # 获取每个样本的预测值
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    # 将准确率记录到 TensorBoard
    writer.add_scalar('Accuracy/test', accuracy, epoch)
    return accuracy


# 5. 对某个样本进行分类预测
def predict(model, sample, device):
    model.eval()  # 切换到评估模式
    with torch.no_grad():  # 预测时不需要计算梯度
        sample = torch.tensor(sample, dtype=torch.float32).to(device)
        output = model(sample)
        _, predicted = torch.max(output, 1)  # 获取预测结果
        return predicted.item()


# 主函数
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 创建 TensorBoard 写入器
    writer = SummaryWriter(log_dir='/root/tensorboard-logs')

    # 生成随机训练和测试数据
    X_train, y_train = generate_data(800)  # 生成800个训练样本
    X_test, y_test = generate_data(200)  # 生成200个测试样本

    # 将数据封装为TensorDataset
    train_dataset = TensorDataset(X_train, y_train)
    test_dataset = TensorDataset(X_test, y_test)

    # 使用DataLoader加载数据
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # 创建网络模型
    model = SimpleNet().to(device)

    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()  # 使用交叉熵损失
    optimizer = optim.SGD(model.parameters(), lr=0.01)  # 使用随机梯度下降优化器

    # 训练模型
    train(model, train_loader, test_loader, criterion, optimizer, device, writer)

    # 对某个样本进行分类预测
    sample = [[7.5, 3.0]]  # 商品的价格为7.5，评分为3.0
    prediction = predict(model, sample, device)
    print(f'对于样本 {sample} 的预测结果为: {"受欢迎" if prediction == 1 else "不受欢迎"}')

    # 关闭 TensorBoard 写入器
    writer.close()


if __name__ == "__main__":
    main()
