import string
import re
import math
import requests

CIPHER = 'ERZCDZXLUPSFCNIFTGGLWBHIZAKLKZSGXOIUALKCLBUPXSFYRRAECRWQBHHKFMNQXYNYEYMEXOKCXIHLGMBPKEXMPYLACPQDHHIOJHLOYJXYZZDBWKDLAUPZAIMQSUTFNOVFSUODYJKZSGXEKEXNQLWVUNVWWJKZAZCXOHBLTSHTMOIXTNJOJLZCWAESPKEXIPDZXUWDZHLKDQHZJSKMIOLKMIPOSGXOIKBMVOJFLUTGXACBYXLAGZHGCBJBYFDZXVNKUDMOSLAUUSFXPGBKTQOIXTNJOJHLOIEHNJOJTHFXWOYTCSPUPIDBEGXWLMQPWBNJOJHZVRWFZQBLAYKBVTSUGWKYNYFZVGPGKYVRWWUACGYJJYLHATKHAMOIXBLUDXTHESWLLGQSKXKXYPBCDLAYAGWKYNSCXQGBWNHTOSLIPKTESFOJBPGNXKIODZXCTDGFVUDGGYUDZXMJKHXIHDZXFGDLXLUYFFSHKLAYTCYTPGWWTHQNVBXGKLAUVRWPUUKKJOCBWLNQELWUTUETHYSLAWWBDRVNKUDBCSJYLQWLAYERSKUEDWKUPNLNLPYXMBGSFLWTSHMCQXSEMQQWHLISSGUYSXXIHDZXUDYNXCFBWPUERAEXKCZVIPMDNMKYFMBCDERGQDZXLYKKYLGMCEYFKFWMKMCESVYXBPGVAMNNOKMIPODHTGXYXMGKUAUDYMMUHYGMUPNSAUNPDHHIGZBWJGWKYCBJTHIOVBHCXWTNTYOUYUSVXNJOAKATKNXUPNOXLGCSVLGNLHNJOEXGQBQHZHSNXFKDLEYDBGMBGBKHZOSFXQJYYTPGEHMLASFZNQQWMUNSNBHIOPVYGNAGANIWTLNIAGNJKLNHKFWKMCVKMLWQYEYKKEBHFOTMYFPGKUDODBYHSJXFKQAHOUVQXHVOJMUKXWWNJKLMBGIZTXCVDUYGXTHLPYFMBGSJUUEUKPCVRLAYKBZTHFCAGNJOAKNTYMLYTCHHWMOLLUPNZTXPONXLVKCXHVRWFIWDAGNJSKLNCDWHZGHALNGXUXIWBKPUUDZXGCBKAWQEFMLANGPHDILAYTSNXLYSLACPKKMBGBAOYTGGNHFDOXHVIEBFGCGYNJOKXUOIXBLUDEHMVFAOCFKFWVTYSWCOZJXMUSGGIHDZXCFOFMCVIGYNJSFZMUOWFMVYEXNQRSOYDOWGACSFXXQXSFYOYJTVNOJTQCPLXLPYGGNQGSKXUONXHKXYTNUEUAUVSEXCHYMGXQELYITMWKNCSFMBCDLACULDXUMZDTWGYNXLIBGPHYSLAHGDLEYUGSLNJOUAOTMZRUTNSGXVRSMJJSDBJRSJKCRVSMYQPLACUZSKCURSGXCVKHAGYJZCCXSPCHOGYNJOSUIXOOXLGNWTXCXVUOTSWWUPNLAUVKDXRCXVXLDKJMBQVGFYYKTKUJKEMIDSSLUPNJHAGBAGZCXLVBKVVKYPYXMBGKXHLGCSBXYOJXUNCGWYCNSGXDEJBYFKFWNJKLMBGNSKEHVSMQKVVXLPOKLVGIGGXVRWVBWBUASCBVBHVOJLYEDWWQKDZWSMOKTHFWGNHFCSGXIKLXMYSLAMEKLMYTOVVUVDDXZGOVBHIYFBNYKKMBGWSKMJOKTHFDZTNVRWEIYVWTXGXDBHGLWRIPNOTMVRWKCXOJTHFDZTNVRWWCUDSGNUKNTAGVSBLHBGFQJSUANJOOBHFGSLLWCZBHIGSLNJOKXUCXVMBCDLAYUWSEFDEFWFGYXLBKFWKMIBGPCPQSYLCSVHZKDSEFCXVUYISFGCPQLHWTIOTMRSHAINNQHOTXGBMGMJBYFKLXLTSTEYXYAVYCCSFUPCLTLVOVNJHBGFUOYFZNJOYKUXOKTNVRWLCFOGYNJOUAOTMZIITMZDYGZKMCNVQHONSLMFGNWOCNYJBFNMMMSQEJMBTYSMUHOSKZWVETHCVDBHEYSKMGQJXSYSLAUIBWTNKBGGIPRALFGQSFUPGAMBPYZTNCXVPCVR'
CIPHER = "Mbvr dep nyx wmxm Z'op xhfu, flox nybykl lzzsx uywhci B'g feoRhnybyk eywm qsk ojmzwts, skzoxh uhhrhh kap jkyvplcKirwdmwy Z lpi mbzgrwvfvtcikYpx es xsv msvhoxa xc kyrkgmxq dbcvhlJelzx nf msi kirw, dxnwb uj choi lthxC'd gzxacez mym u gtdwxhxxc eeiez qsk nyx cmwyZ'f ysmbzgr fnn r ilwlyezpv tffgr jhl kap vbxvXji mi vrp xalfnrl fs ixlvocvp xmklfkRimnzgr wfucepv tm Z wtwtjgxlvLouwpres vopvrnybyk bm jh xyvb tepekyiTyh tfc B'x pxzk ptxa cj fj khiu ycmxhu ypekUew avhgzlpw hz kxlvl, uew avhgzlpw hz kxlvlNyxj wtq kap pbyj B'gi micw, xedy katrzm ibrlm vvyzvx C'd hwhGikatrz fvye jhl ll es lup, ucsdye wzag ie msi ylvxherLftowbxv B dix nybykl wcxlvxlVrp xh ypx elkilzs qr lvtczbyn ftvkiiLweoy kh elx lfto, wmotd mc rilk dmwyZ'f ysmbzgr fnn r ilwlyezpv tffgr jhl kap vbxvB'x rhnybyk uok t aelmvgrik uchyk yii msi kcuxPcx nf xji mbihfka gp kpekpzxh qblihcKxnkbyk lgrewik uj B omlugipekMlwoigfp xgikskatrz cj lz qnwy vwitlvkLrw uce T'q eywm hmmb zl xc zifw qvbyew qitlRgo tkidbdil iw mpekm, rgo tkidbdil iw mpekmDhyhts zl l vtcer oerUew T wmup bywbxv, epxmcez emfy gtdw tqrrEyxmutj mm cj jfmmy kap wtgvLz M wupwcitg ruzym gffprmm fy dltgvEtjx afxd ekilgo egx 'ihfrwC'mx dxngseph thu lesijvw xsocez zrMoig lvhoew lrw C ixlpbtvwEltn Z alzx vvxy pxzk uplbhuBy e mcer emgs, kbyc, mcer nyuctepXayix wmoyj t hlbhp, psmgs, natrr wfplvwfp mfvmfvBy xpyemj, xacimj, jhlkr, qmynp, ltbms pxlvlGp apekn nhy'x wcv, gz qtnkxc lhq ytch B nirEswup bd e eiexwc wupB avxnvgo xauk B citfcr wmdyu be xacj plcMidhcvhq nbwp lnrr elx mrfpEgx Z vlr'm ymxy vxgvfmik sfnc rtgvRzy'ky rkzygx eh xsky, eh xskyKazyzb katw eimx zj fcexTx cojm hsg'n jmztGishoc-uiur-msws-shoc mi jnathlkFj lxumr, sitpp, apeos sne ifjkr dlxfcUfx B'g ehe pttp, eldr, frsj, pttp tycfiixZl wuietrz wrg'e cho jxpM'oy xkzag mf ffga gfkpQtssx, xervv, flcuy phf'zx zfkrmoye fpSa vlm oekfzgr, htlcbyk, wuietrz sfn seoy kh xedy jnciMi jmlf fy, gbpvvy dx, sykn dx, vmef dx elhlfnrlesPhf wxy dr sitlk pzr'm xzx elhoxa T vxucej xkcvwJsn mvx T rxpvk frwyileshxNaj M'f mlvs e plvvv sk qyr tx yyved wh afhoM hhcr os mbzgrw mbrm aihjcx elbhb B dlhocwT rxpvk cieuo, B ryxmj B yioyi vzyexRgo M wie'm vrhq yhhLhq zm pzxl vgoiw og etox nybdM zovld jhl rew xacj mtqx C bgpaB qrl tr viemcseC ntd phmzgr xhotaLrw hfp T knyjl elx ieej xacez es wiZl es lyce xc lile lrw ck pzr'm mvew jhl dnnlB wrg'e fxfzxgi yii twp mbzl emfy Z dyipC ntd mg wfgevhfZ plw eijbyk milvsEgx pxll, B alxdw mbv hypr nybyk mi uhTw mi jxwp fs jhfpThu plxvb zm rs ecbxLrw ck'l l waudxT wxfuhx tkutmtgx qyte M ilvtnlEcwx tw t ffgr-waik jfiln whc qxuebykBn'j ty ykavgnc B'g wxppbhxB ryxmj B nsnfu dpii vvetiocezTj B nfhv xay kbxi mi kkjEgx Z'f ysm wfgnikhvw hmmb mbcxnyXnpwl C'mx rsm u che xh qfkv xalfnrlThu B'o rxpvk xith kh sykn phfXailzs M'oy exgik ymxy xkcvwSir, vcnp wds kboi ayci xi vfvtc qr gzgoJnfc hq rhnybyk B hvxo, rhC chzo nj jhximcdxd egx kh xc loiicmlyZ vlr ycetwpr vixlxay, nhllBn'j t citf katr ecex 'eaxye plwmcez emfyRgo kxnkbyk lidx aitwv mssnayTwp mbv wptmbj B omoy kkj xh zzglpes wbyh hokPsem ck twp fyrgdSa zrbelyocByrxl uxxsgmXbgi fy jhximbzgr xh vvetioy zgT'zx vvxy wmoduwmga 'ihfrw nyx pxayiB vixj nhyhxlzgr aas Z'f siky"
CIPHER = CIPHER.upper().replace(' ','').replace(',','').replace("'",'').replace('.','').replace('-','')
print(CIPHER )

ENG = 0.0667
RAND = 1/26

# (a)
# Friedman II
def friedmanII(text):
    phi = 0
    # phi = sum(probabilities of each letter)
    for c in string.ascii_uppercase:
        phi += (text.count(c)/len(text))**2
    return phi, len(text)*(ENG-RAND)/((len(text)-1)*phi-len(text)*RAND+ENG)

print(f"estimated key length: {friedmanII(CIPHER)[1]}")






# (b)
# Kasiski's test
tri = {}
# count num of occurence for each triple
for i in range(len(CIPHER) - 2):
    tri[CIPHER[i:i+3]] = tri.get(CIPHER[i:i+3], 0) + 1

distance = []
print("\ntext | First occur | Distance to Subsequent Occurences")

# take the top 5 most frequent triples
for t in sorted(tri, key=tri.get)[-5:]:
    # index of all occurences
    occ = [m.start() for m in re.finditer(t, CIPHER)]
    # text | First occur | Distance to Subsequent Occurences
    print(f" {t} |     {occ[0]}     | {[i-occ[0] for i in occ][1:]}")
    distance += [i-occ[0] for i in occ][1:]

# key length = gcd of all Distance to Subsequent Occurences
print(f"\nthe most likely length of the key = {math.gcd(*distance)}")


















# (c)
# Decryption
# 5-letter English words
meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
# compile regex
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
# find all matches
words = [w.upper() for w in pattern.findall(meaningpedia_resp.text)]

# test out each word as keyword
for w in words:
    plain = ''
    for i, c in enumerate(CIPHER):
        # subtract the index of the corresponding keyword character  
        # from the index of the cipher text character
        # modulo 26 to get a valid index in the alphabet
        # add the plaintext character at the index to string
        plain += string.ascii_uppercase[(string.ascii_uppercase
            .index(c)-string.ascii_uppercase.index(w[i%5]))%26]

    # filter the result by comparing its phi value to that of English
    if abs(friedmanII(plain)[0] - ENG) <= 0.005:
        print(f'\nkeyword: {w}\nplain text: {plain}\n')







