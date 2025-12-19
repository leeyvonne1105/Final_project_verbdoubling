This project is based on this paper  
[Mandarin verbdoublingasverb-phrasefronting by Jackie Yan-Ki Lai](https://www.researchgate.net/publication/386021091_Mandarin_verb_doubling_as_verb-phrase_fronting)    
I have produced codes that can transform "王小明開車兩小時" into "王小明開車開了兩小時" (in a file called "Loki_verboriginal.py" under "intent" file  
However there are still many unsolved structure that I cannot come up with a solution...

These are the examples I collected from the paper:  


 Mandarin verbdoublingasverb-phrasefronting

他開車開了兩次 v
*他開了車兩次

他看電視看了三個小時 v
*他看了電視三個小時

說明哪個動詞後面可以加"了” : 
張三罵了他兩次  → 張三罵他罵了兩次 V
張三罵了李四兩次 → 張三罵李四罵了兩次 v
張三罵了那個人兩次 → 張三罵那個人罵了兩次
張三罵了一個人兩次 → 張三罵一個人罵了兩次
*張三罵了人兩次 → 張三罵人罵了兩次 (這是合法的句子)

李四騎那匹馬 騎了兩次v
李四騎那匹馬騎了兩個小時 v
騎那匹馬，李四騎了兩個小時
*李四騎那匹馬騎了

他騎那匹馬騎了兩個小時 v
他騎了那匹馬兩個小時
*他騎了那匹馬騎兩個小時
*他騎了那匹馬騎了兩個小時

李四騎了兩次那匹馬
李四騎了那匹馬



李四看電視看三個小時
李四沒看電視有三個小時




動詞後面沒有受詞，所以直接重複動詞不行，但中間加了"可能"就可以使句子變的合法
張三哭了兩次
*張三哭哭了兩次/  張三哭，可能哭了兩次/  哭，張三哭了兩次  v

李四睡了兩次
*李四睡睡了兩次/  李四睡可能睡了兩次 /睡，李四睡了兩次  v

客人來了兩次
*客人來來了兩次 / 客人來可能來了兩次/ 來，客人來了兩次  v

雨下了兩次 v
*雨下下了兩次  *雨下可能下了兩次(“下雨可能下了兩次” 比較順)

Island effect: 
*騎那匹馬，我相信李四騎了兩個小時的說法 (原: 我相信李四騎那匹馬騎了兩個小時的說法)
*騎那匹馬，你和他在李四騎了兩個小時之後才分手 (原: 你和他在李四騎那匹馬騎了兩個小時後才分手)
*騎那匹馬，我聽過李四騎了兩個小時的說法 (原:我聽過李四騎那匹馬騎了兩個小時的說法)
*騎那匹馬，我支持李四每天騎兩個小時的提議 (原:我支持李四每天騎那匹馬騎兩個小時的提議)
騎那匹馬，我知道李四騎了整整兩個小時(原: 我知道李四騎那匹馬騎了整整兩個小時)
(自己想的: *騎那匹馬，我知道李四騎了整整兩個小時的事)
騎那匹馬，我很後悔李四騎了整整兩個小時 (原: 我很後悔李四騎那匹馬騎了整整兩個小時)

ExtractionoftheV–Osequencefromacomplementclauseispotentiallyunbounded otherwise:
騎那匹馬，張三說李四騎了兩個小時 (原: 張三說李四騎那匹馬騎了兩個小時)

張三說李四那匹馬騎了 (原: 張三說李四騎了那匹馬)

verb fronting
*騎馬，李四會三次 (原:李四會騎馬三次)
騎馬，李四會騎三次 (原: 李四會騎馬騎三次)
*騎馬，李四會騎

提前的動詞要是同一個
*李四讀那本書看了六個小時

我可以看三天書
看書我可以看三天
*我可以看書三天書

他買了書，我也買了書
他買了書，我也買了
*他買了，我也買了書

negation:
*李四沒有讀那本書讀(原: 李四沒有讀那本書)
*李四讀那本書沒讀
modal:
*李四可以讀那本書讀
*李四讀那本可以讀

張三趕飛機趕上了
*張三趕上飛機趕上了
*張三趕飛機趕了
張三趕飛機趕上了好幾次
?*張三趕上飛機趕上了好幾次

*張三念那本書三次念了
*李四送瑪莉那份禮物送了

張三騎馬最喜歡騎黑馬
馬，張三最喜歡黑馬

