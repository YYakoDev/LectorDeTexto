import win32clipboard

class ClipboardGetter(object):
    @staticmethod
    def get_clipboard_text():
        win32clipboard.OpenClipboard()
        try:
            #The GetClipboardData function retrieves data from the clipboard in a specified format.
            #The clipboard must have been opened previously. 
            #Note that not all data formats are supported, and that the underlying handle can be retrieved with win32clipboard::GetClipboardDataHandle
            data = win32clipboard.GetClipboardData() 
        except TypeError:
            data = ""
        except:
            data = "ocurrior un error inesperado"
        win32clipboard.CloseClipboard()
        return data