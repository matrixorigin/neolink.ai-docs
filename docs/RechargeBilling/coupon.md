---
sidebar_position: 4
title: Coupons
sidebar_label: Coupons
---

Neolink.AI currently offers two types of coupons: Compute Coupons and Vouchers. Users can navigate to **Billing** -> **Billing Center** -> **Coupons** to view detailed information about available coupons.

**NOTE**: Compute Coupons and Vouchers cannot be used if there are outstanding payments.

## Compute Coupons

After completing the real-name authentication process, new users will receive free compute trial coupons. Please note that these trial coupons come with an expiration date. Users can check the details and usage conditions of their compute coupons on the Coupons page.

<img src={require('../../static/img/billing/coupon-2.png').default} alt="Compute Coupon" style={{width: '600px', height: 'auto'}} />

Click the **Use Now** button next to the compute coupon to be redirected to the instance creation page.

<img src={require('../../static/img/billing/coupon-3.png').default} alt="Use Compute Coupon" style={{width: '600px', height: 'auto'}} />

**NOTE**: After the coupon expires, regular pay-as-you-go pricing will apply. If you do not wish to continue using the instance, simply shut it down before the expiration date.

## Vouchers

Users who make a one-time deposit of a certain amount will receive vouchers. Additionally, vouchers distributed during promotional events can be redeemed using a voucher code. Vouchers can be applied to all Neolink.AI platform products. Voucher details are available on the Coupons page.

<img src={require('../../static/img/billing/coupon-1.png').default} alt="Voucher" style={{width: '600px', height: 'auto'}} />

### Usage Guidelines:

- For eligible products, the system will apply vouchers in the following order:
  - Priority is given to the earliest expiring voucher that can cover the entire order amount.
  - If no voucher can cover the full amount, the earliest expiring voucher will be used.
  - If multiple vouchers expire on the same date, the system will prioritize them based on the smallest deductible amount and remaining balance to provide the best benefit.
- Vouchers must be used before they expire; expired vouchers become invalid.
- Vouchers cannot be exchanged and cannot be used to offset outstanding payments. Therefore, vouchers are unavailable when the account balance is negative.
- No minimum spending is required to use a voucher.
- A voucher can be used multiple times. For example, if a voucher is worth 100 CNY and 30 CNY is used, the remaining 70 CNY can be used in the future.
- Only one voucher can be used per payment, and used vouchers cannot be refunded.
- For pay-as-you-go instances, vouchers will be deducted first. If the voucher balance is insufficient, the remaining amount will be deducted from the account balance.
- Vouchers cannot be used for instances with the following plans:
  - 6-month or longer 4090 instances
  - 12-month H100 instances
  - H20 instances
  - 3090 instances
