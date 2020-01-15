
import wx
import wx.xrc
from search import _search_doc


class MyFrame2 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            519, 532), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        wSizer1 = wx.WrapSizer(wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"The Search", wx.DefaultPosition, wx.Size(500, -1), wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(
            20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI"))
        self.m_staticText3.SetForegroundColour(wx.Colour(0, 128, 64))
        wSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.txbSearch = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 30), 0)
        self.txbSearch.SetFont(wx.Font(
            11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI"))
        self.txbSearch.SetForegroundColour(wx.Colour(0, 128, 64))
        self.txbSearch.SetBackgroundColour(wx.Colour(255, 255, 255))

        wSizer1.Add(self.txbSearch, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(
            self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size(500, -1), wx.BORDER_NONE)
        self.m_button10.SetFont(wx.Font(
            11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI"))
        self.m_button10.SetForegroundColour(wx.Colour(0, 128, 64))
        self.m_button10.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        wSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.txbNumberTopic = wx.TextCtrl(self, wx.ID_ANY, u"Số topics: 0", wx.DefaultPosition, wx.Size(
            500, -1), wx.TE_CENTER | wx.TE_READONLY)
        self.txbNumberTopic.SetFont(wx.Font(
            11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI"))
        self.txbNumberTopic.SetForegroundColour(wx.Colour(0, 128, 64))

        wSizer1.Add(self.txbNumberTopic, 0, wx.ALL, 5)

        self.txbResult = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, 300), wx.TE_MULTILINE)
        self.txbResult.SetForegroundColour(wx.Colour(0, 128, 64))

        wSizer1.Add(self.txbResult, 0, wx.ALL, 5)

        self.SetSizer(wSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button10.Bind(wx.EVT_BUTTON, self.search)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def search(self, event):
        docs = _search_doc(self.txbSearch.GetValue().split())
        if len(docs) == 0 :
            self.txbNumberTopic.SetValue('Số topics: 0')
            self.txbResult.SetValue('Không tìm thấy kết quả phù hợp')
            return
        self.txbNumberTopic.SetValue('Số topics: {}'.format(len(docs)))
        text = ''
        if docs:
            for doc in docs:
                text = text + doc + '\n------------------------------------------------------------------------------\n'

        self.txbResult.SetValue(text)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame2(parent=None)
    frame.Show()
    app.MainLoop()
