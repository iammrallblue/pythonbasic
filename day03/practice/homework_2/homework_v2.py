# coding:utf-8
# 3/23/21 10:06 AM

"""
    split the string str_value
"""
str_value = "symbol=BCHBTC;baseCoin=BCH;quoteCoin=BTC;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=QTUMUSDT;baseCoin=QTUM;quoteCoin=USDT;baseAccountNormal=201143;baseAccountLock=202143;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101360;sysQuoteAccount=101361;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101362;useFeeByAward=false;feeAccountAward=206109-symbol=BCHUSDT;baseCoin=BCH;quoteCoin=USDT;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=BOTBTC;baseCoin=BOT;quoteCoin=BTC;baseAccountNormal=201145;baseAccountLock=202145;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101121;sysQuoteAccount=101122;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101123;useFeeByAward=false;feeAccountAward=206109-symbol=ETHBTC;baseCoin=ETH;quoteCoin=BTC;baseAccountNormal=201102;baseAccountLock=202102;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101011;sysQuoteAccount=101012;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101023;useFeeByAward=false;feeAccountAward=206109"
print(str_value.split(";"))  # return a list as below
'''
['symbol=BCHBTC', 'baseCoin=BCH', 'quoteCoin=BTC', ...'useFeeByAward=false', 'feeAccountAward=206109']

'''
for i in str_value.split(";"):
    if i.startswith("symbol"):
        file_name = i.split("=")[-1] + ".yml"  # get file name
        print(file_name)
        print(i.replace("=", ": "))
        new_file = open(file_name, "w", encoding='utf-8')
        new_file.write(i.replace("=", ": ") + "\n")  # ONLY write symbol, b/c of condition
        pass
    # elif i.startswith("-symbol"):
    #     left_hyphen, right_hyphen = i.split("-")
    #     print(left_hyphen)
    #     print(right_hyphen)
    #     file_name = right_hyphen.split("=")[-1] + ".yml"
    if "-symbol" in i:  # get file names
        left_hyphen, right_hyphen = i.split("-")  # separated by "-" hyphen
        # print(left_hyphen)
        # print(right_hyphen)
        print(left_hyphen.replace("=", ": "))
        print("*" * 30)
        file_name = right_hyphen.split("=")[-1] + ".yml"
        print(file_name)
        print(right_hyphen.replace("=", ": "))
    if "symbol" not in i:
        # print(i)
        print(i.replace("=", ": "))
        new_file.write(i.replace("=", ": ") + "\n")
        # print(i)
        pass

print("*" * 50)
