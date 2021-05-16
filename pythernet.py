import wmi
c = wmi.WMI()
o = c.query("select * from Win32_NetworkAdapter where NetConnectionID='Ethernet'")[0]

if o.NetEnabled:
	o.Disable()
else:
	o.Enable()
