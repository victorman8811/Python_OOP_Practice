# Python_OOP_Practice



題目說明：

你好！冒險者！在前方叢林裡有一隻邪惡的魔獸，非常兇險可怕
......
這段日子村民都無法上山狩獵、採食，生活大受影響
......
我相信你可以擊敗他，為村子帶來和平！
冒險者！你將被賦予三隻魔物
1. 哥布林，血量 40，攻擊力 15
2. 火精靈，血量 80，攻擊力 15，護盾 35
3. 惡狼犬，血量 50，攻擊力 20，護盾 15

至於叢林內的魔獸，根據村中獵手判斷魔獸極為強大
擁有血量
220，攻擊力 30
找到魔獸弱點，打敗魔獸吧！


--------------------------------------
程式撰寫提示與規則：
1. 你是一位冒險者，並擁有魔物
2. 每個魔獸都有自己的屬性與特質
3. 一次只能派一隻魔物與魔獸打鬥
4. 攻擊力與血量的計算範例：血量 50 被 攻擊力 10 攻擊一次後，血量剩下 40。 (50-10=40)
5. 若有護盾，則先扣護盾再扣血量
6. 攻擊順序採回合制，並保證輪流，如：冒險者 ->魔獸 ->冒險者 ->魔獸 ...不斷循環
7. 冒險者必為先攻
8. 冒險者的魔物上場順序為隨機上場
9. 魔物一但上場 ，必須戰死後才能換下一隻
10. 殺死魔獸則勝利，魔物全數戰死則失敗
程式範例輸出：
戰鬥開始！
火精靈上場
對敵方進行攻擊，敵方所剩血量
205，護盾 0
敵方襲擊猛烈，火精靈所剩血量
80，護盾 5
對敵方進行攻擊，敵方所剩血量
190，護盾 0
敵方襲擊猛烈，火精靈所剩血量
55，護盾 0
(...以下省略 ...)
火精靈戰死
哥布林上場
對敵方進行攻擊，敵方所剩血量
xxx，護盾 xxx
(...以下省略 ...)
戰鬥勝利！
--------------------------------------
