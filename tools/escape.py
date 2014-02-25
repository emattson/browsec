import base64
import sys
from AppKit import NSPasteboard, NSArray

pb = NSPasteboard.generalPasteboard()
pb.clearContents()
encoded = base64.urlsafe_b64encode(str(sys.argv[1]))
pb.writeObjects_(NSArray.arrayWithObject_(encoded))