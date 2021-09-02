# IpPhonesAlcaltelTelnet

1. Python script (main.py) identifies "C: \ Temp \ MD5.xls" and reads all ips in column 1 (B),  telnet session on this IPs and execute these commands:
> - `dot1x` : indetify tls status (DISABLED / ENABLED)
> - `dot1x tls on` : tls active if disabled
> - `reset` : reset phone

2. Log file (IpPhonesAlcaltelTelnet.log) in script folder!
3. Shell Script (EnableTelnet) for allow telnet from extension number from a list!
- Create folder: `mkdir/DHS3bin/mtcl/scripts /`
- Copy EnableTelnet into this folder (/DHS3bin/mtcl/scripts/)
- Create file (extension numbers): `vi list_extension`
- Permission in script: `chmod + x EnableTelnet`
- Command used in script: `/usr2/oneshot/mtcl/ tool ippstat telnet d $ ip t 1440`
