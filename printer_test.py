from escpos.connections import getUSBPrinter


printer = getUSBPrinter()(idVendor=0x1504,
                          idProduct=0x0006,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01)# Create the printer object with the connection params

printer.text("Hello World")
printer.lf()


# # find our device
# import usb
#
# dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)
#
# # was it found?
# if dev is None:
#     raise ValueError('Device not found')