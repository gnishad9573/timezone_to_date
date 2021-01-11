import datetime
output = "Fri Jan  8 02:32:49 EET 2021"
date_format_list = output.split(" ")
timezone = ["IST","GMT","EST","UTC","ECT","EET","ART","EAT","MET","NET","PLT","BST","VST","CTT","JST",\
            "ACT","AET","SST","NST","MIT","HST","AST","PST","PNT","MST","CST","EST","IET","PRT","CNT",\
            "AGT","BET","CAT"]
pattern_timezone = '%a %b %d %H:%M:%S %Z %Y'
match_time_zone = ""
for i in timezone:
    if i in date_format_list:
        print(i)
        match_time_zone = pattern_timezone.replace("%Z", i)
print(match_time_zone)
date_format = datetime.datetime.strptime(output, match_time_zone).strftime("%d/%m/%Y")
