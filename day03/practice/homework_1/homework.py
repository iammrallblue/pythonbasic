# coding:utf-8
# 3/22/21 9:44 PM
"""
    instance:
        to split the string str_value
            symbol=BCHBTC;baseCoin=BCH;quoteCoin=BTC;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=QTUMUSDT;baseCoin=QTUM;quoteCoin=USDT;baseAccountNormal=201143;baseAccountLock=202143;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101360;sysQuoteAccount=101361;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101362;useFeeByAward=false;feeAccountAward=206109-symbol=BCHUSDT;baseCoin=BCH;quoteCoin=USDT;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=BOTBTC;baseCoin=BOT;quoteCoin=BTC;baseAccountNormal=201145;baseAccountLock=202145;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101121;sysQuoteAccount=101122;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101123;useFeeByAward=false;feeAccountAward=206109-symbol=ETHBTC;baseCoin=ETH;quoteCoin=BTC;baseAccountNormal=201102;baseAccountLock=202102;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101011;sysQuoteAccount=101012;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101023;useFeeByAward=false;feeAccountAward=206109

        change the string to form:
            ***
                symbol : BCHBTC
                baseCoin : BCH
                quoteCoin : BTC
            ***
    Steps:
        1. split()
            Return a list of the words in the string, using sep as the delimiter string.
        2. enumerate()
            Return an enumerate object.
            iterable
                 an object supporting iteration
"""

str_value = "symbol=BCHBTC;baseCoin=BCH;quoteCoin=BTC;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=QTUMUSDT;baseCoin=QTUM;quoteCoin=USDT;baseAccountNormal=201143;baseAccountLock=202143;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101360;sysQuoteAccount=101361;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101362;useFeeByAward=false;feeAccountAward=206109-symbol=BCHUSDT;baseCoin=BCH;quoteCoin=USDT;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109-symbol=BOTBTC;baseCoin=BOT;quoteCoin=BTC;baseAccountNormal=201145;baseAccountLock=202145;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101121;sysQuoteAccount=101122;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101123;useFeeByAward=false;feeAccountAward=206109-symbol=ETHBTC;baseCoin=ETH;quoteCoin=BTC;baseAccountNormal=201102;baseAccountLock=202102;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101011;sysQuoteAccount=101012;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101023;useFeeByAward=false;feeAccountAward=206109"

# split str_value by for split() function and loop statement
# for idx, i in enumerate(str_value.split("-"), 1):
#     # print(i)  # print out result in multiple lines and started with word "symbol"
#     # file_name = str(idx) + ".yml"
#     file_name = i.split(";")[0].split("=")[1] + ".yml"
#     print(file_name)
#     print("*" * 30)
#     # str_changed = i.replace("=", ": ").replace(";", "\n")
#     # print("After changing:", str_changed)
#     # break
#     pass

'''
Version one: to split a str, to save content into a few new files, and take names from the content

print(str_value.split("-")) # separate by "-"
['symbol=BCHBTC;baseCoin=BCH;quoteCoin=BTC;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109', 'symbol=QTUMUSDT;baseCoin=QTUM;quoteCoin=USDT;baseAccountNormal=201143;baseAccountLock=202143;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101360;sysQuoteAccount=101361;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101362;useFeeByAward=false;feeAccountAward=206109', 'symbol=BCHUSDT;baseCoin=BCH;quoteCoin=USDT;baseAccountNormal=201104;baseAccountLock=202104;quoteAccountNormal=201106;quoteAccountLock=202106;sysUid=1;sysBaseAccount=101015;sysQuoteAccount=101016;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101025;useFeeByAward=false;feeAccountAward=206109', 'symbol=BOTBTC;baseCoin=BOT;quoteCoin=BTC;baseAccountNormal=201145;baseAccountLock=202145;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101121;sysQuoteAccount=101122;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101123;useFeeByAward=false;feeAccountAward=206109', 'symbol=ETHBTC;baseCoin=ETH;quoteCoin=BTC;baseAccountNormal=201102;baseAccountLock=202102;quoteAccountNormal=201101;quoteAccountLock=202101;sysUid=1;sysBaseAccount=101011;sysQuoteAccount=101012;feeCoin=YLB;useFeeCoin=false;feeAccountNormal=201109;sysFeeAccount=101023;useFeeByAward=false;feeAccountAward=206109']
    # print(i.split(";")[0])  # "i.split(";")[0]" = symbol=BCHBTC
    # print(i.split(";")[0].split("=")[-1]) # BCHBTC
    # get_name = i.split(";")[0].split("=")[-1] + ".yml"  # separated again, by ";" and "="
    # print(get_name)
        BCHBTC.yml
        QTUMUSDT.yml
        BCHUSDT.yml
        BOTBTC.yml
        ETHBTC.yml
'''
for i in str_value.split("-"):  # "str_value.split("-")" is a list
    # print(i) # print out result separated by "-"
    # to get name from the string
    get_name = i.split(";")[0].split("=")[-1] + ".yml"  # separated again, by ";" and "="
    # print(get_name)
    file_content = i.replace("=", ": ").replace(";", "\n")
    new_file = open(get_name, "w", encoding='utf-8')  # open() a file, in "w"(write) mode
    new_file.write(file_content)
    new_file.close()
    # break
    pass

# # list_a = ["a", "b", "c", "d", "e"]
# list_a = str_value.split("-")  # "str_value.split("-")" is a list
# for ind, i in enumerate(list_a, 1):
#     print(ind, i)
#     pass
# '''
# 1 a
# 2 b
# 3 c
# 4 d
# '''
