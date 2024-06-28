import gmail
import datetime

g = gmail.login("tomekmakow", "fwjh hbln vnge mfda")
g.inbox().download_metadata(after=datetime.date(2024, 6, 26))