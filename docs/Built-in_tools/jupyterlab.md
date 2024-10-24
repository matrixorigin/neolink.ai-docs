---
sidebar_position: 1
title: JupyterLab
sidebar_label: JupyterLab
---

## What is JupyterLab?

JupyterLab is a flexible user interface designed for creating and sharing computational documents, especially useful in areas such as data science, machine learning, scientific computing, and education. As the next-generation interface for Jupyter Notebooks, JupyterLab offers richer and more extensible features.

It integrates various tools, such as code editors, terminals, text editors, file browsers, and notebooks, allowing users to switch between different tools within a single interface without juggling multiple windows. Additionally, JupyterLab supports multiple programming languages, including Python, R, Julia, and Scala, enabling cross-language development and experimentation in the same environment without the need to install multiple development environments.

All Neolink images currently come with JupyterLab as a built-in tool, helping users enhance productivity whether performing complex data analysis, training machine learning models, or conducting everyday programming tasks.

## Application Scenarios

- **Data Science and Analysis:** Data scientists can use JupyterLab for data cleaning, analysis, and modeling, making it easier to handle and visualize data.
- **Machine Learning and Deep Learning:**
  - JupyterLab supports machine learning libraries such as Scikit-learn, TensorFlow, and PyTorch, facilitating model building, training, and evaluation.
- **Education and Training:**
  - Suitable for teaching, as instructors can create interactive lessons, and students can experiment and learn in real-time.
- **Scientific Research:** Researchers can use JupyterLab to document experiments, analyze results, and generate reproducible research documents.
- **Rapid Prototyping:** Developers can leverage JupyterLab to quickly prototype applications, test, and iterate on ideas.

## Steps to Use

Access the **Compute Instances** from the left sidebar, and under the built-in tools of the specific instance, click **JupyterLab** to enter the JupyterLab interface.

<img src={require('../../static/img/qa/ssh-interrupt-1.png').default} alt="" style={{width: '600px', height: 'auto'}} />

<img src={require('../../static/img/jupyterlab/jupyterlab-2.png').default} alt="JupyterLab Interface" style={{width: '600px', height: 'auto'}} />

## Basic Features

The JupyterLab interface mainly consists of two parts: the File Browser and the Workspace.

<img src={require('../../static/img/jupyterlab/jupyterlab-3.png').default} alt="JupyterLab Interface" style={{width: '500px', height: 'auto'}} />

In the File Browser, double-click the folder name to navigate into directories. Click the file upload icon to select files for upload.

<img src={require('../../static/img/jupyterlab/jupyterlab-4.png').default} alt="JupyterLab Interface" style={{width: '200px', height: 'auto'}} />

Right-click on a specific folder or file in the File Browser to manage files.

<img src={require('../../static/img/jupyterlab/jupyterlab-5.png').default} alt="JupyterLab Interface" style={{width: '300px', height: 'auto'}} />

In the Workspace, click **Other > Terminal** to open a new terminal. JupyterLab does not terminate processes by default, even after closing terminal or notebook tabs.

<img src={require('../../static/img/jupyterlab/jupyterlab-6.png').default} alt="JupyterLab Interface" style={{width: '500px', height: 'auto'}} />
