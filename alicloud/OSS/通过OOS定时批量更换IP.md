先准备好批量释放ip和批量绑定ip的模板，执行测试。
先给指定的主机批量解除绑定EIP，并释放EIP，然后给主机申请EIP，并绑定。
使用OOS定时运维，需要创建RAM角色
在定时运维中选择创建，选择按周期执行 先释放ip，过几分钟再绑定ip。
创建好后直接触发测试，是否正常工作。确认一切正常后，后续通过OOS自动定期更换EIP。