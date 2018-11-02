import wx
import gui
import pickle
from wx.lib.pubsub import pub

class Instillinger(gui.Instillinger):
    def __init__(self, parent):
        gui.Instillinger.__init__(self, parent)

    def gem(self, event):
        priser = [int(self.pizzaPris.GetValue()), int(self.burgerPris.GetValue()), int(self.colaPris.GetValue())]
        pub.sendMessage("Update", priser = priser)
    
class Oversigt_mad(gui.Oversigt_mad):
    def __init__(self, parent):
        gui.Oversigt_mad.__init__(self, parent)
        self.bestilling_list.InsertColumn(0, "Navn")
        self.bestilling_list.InsertColumn(1, "Pizza")
        self.bestilling_list.InsertColumn(2, "Buger")
        self.bestilling_list.InsertColumn(3, "Cola")
        self.bestilling_list.InsertColumn(4, "Pris ialt")
        self.index = 0

    def add(self, data):
        self.bestilling_list.InsertItem(self.index, data["Navn"])
        self.bestilling_list.SetItem(self.index, 1, str(data["Pizza"]))
        self.bestilling_list.SetItem(self.index, 2, str(data["Burger"]))
        self.bestilling_list.SetItem(self.index, 3, str(data["Cola"]))
        self.bestilling_list.SetItem(self.index, 4, str(data["Pris"]))
        self.index+=1

class madFrame(gui.MadFrame):
    def __init__(self, parent):
        gui.MadFrame.__init__(self, parent)
        self.priser = [45, 45, 12]

    def totalPris(self):
        pris = 0
        for i, n in enumerate([self.pizza_choice.GetSelection(), self.burger_choice.GetSelection(), self.cola_choice.GetSelection()]):
            pris += self.priser[i]*n
        return pris

    def bestil( self, event ):
        pris = self.totalPris()
        pub.sendMessage("bestilling", varer = {"Navn": self.nametxt.GetValue(),
                                               "Pizza": self.pizza_choice.GetSelection(),
                                               "Burger": self.burger_choice.GetSelection(),
                                               "Cola": self.cola_choice.GetSelection(),
                                               "Pris": pris})
    def slut_mad(self, evnet):
        pub.sendMessage("Done")

    def updatePris(self, event):
        pris = self.totalPris()
        self.pris.SetLabelText(str(pris)+",- kr")
    
class mainFrame(gui.MainFrame):
    def __init__(self, parent):
        self.filename = "config.ini"
        gui.MainFrame.__init__(self, parent)
        self.madFrame = madFrame(self)
        self.oversigt_mad = Oversigt_mad(self)
        self.instillinger = Instillinger(self)
        pub.subscribe(self.bestiller, "bestilling")
        pub.subscribe(self.skjuler, "Done")
        pub.subscribe(self.update, "Update")
        try:
            file = open(self.filename, "rb")
            l = pickle.load(file)
            self.update(l)
            file.close()
        except:
            pass

    def bestiller(self, varer):
        self.oversigt_mad.add(varer)
        
    def skjuler(self):
        self.madFrame.Hide()
        self.oversigt_mad.Hide()

    def update(self, priser):
        self.madFrame.priser = priser
        self.instillinger.Hide()
        self.madFrame.pizzaPris.SetLabel(str(priser[0])+",- kr.")
        self.madFrame.burgerPris.SetLabel(str(priser[1])+",- kr.")
        self.madFrame.colaPris.SetLabel(str(priser[2])+",- kr.")
        
    def close( self, event ):
        self.priser = self.madFrame.priser
        file = open(self.filename, "wb")
        pickle.dump(self.priser, file)
        file.close()
        exit(0)

    def mad( self, event ):
        self.madFrame.Show()
        self.oversigt_mad.Show()

    def indstil(self, event):
        self.instillinger.pizzaPris.SetValue("")
        self.instillinger.burgerPris.SetValue("")
        self.instillinger.colaPris.SetValue("")
        self.instillinger.Show()

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
#exit(0)
