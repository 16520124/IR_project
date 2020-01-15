import wx
import wx.xrc
from Project.dataSet import *


class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(824, 369), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"POS TAGGING", wx.DefaultPosition, wx.Size(900, -1),
                                           wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(
            wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI"))
        self.m_staticText1.SetForegroundColour(wx.Colour(221, 11, 142))

        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(900, 100),
                                       wx.TE_MULTILINE)
        self.m_textCtrl5.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI"))

        bSizer3.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size(900, -1),
                                   0 | wx.BORDER_NONE)
        self.m_button4.SetFont(
            wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI"))
        self.m_button4.SetForegroundColour(wx.Colour(221, 11, 142))
        self.m_button4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer3.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(900, 100),
                                       wx.TE_MULTILINE)
        self.m_textCtrl6.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI"))

        bSizer3.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button4.Bind(wx.EVT_BUTTON, self.meowmeow)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def meowmeow(self, event):
        hmm = HMM()
        pages = self.m_textCtrl5.GetValue().lower().split('.')
        text = ''

        for page in pages:
            words = page.strip().split(' ')
            index = 0
            pos = hmm.cal_hmm(words)

            for word in pos:
                if len(words) > index:
                    text = text + '{' + ' ' + words[index] + '\\' + word + '}' + '  '
                else:
                    break
                index = index + 1
            text = text + '. '
        self.m_textCtrl6.SetValue(text)




if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame3(parent=None)
    frame.Show()
    app.MainLoop()
