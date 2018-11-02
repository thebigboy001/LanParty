# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LANparty Administration", pos = wx.DefaultPosition, size = wx.Size( 585,387 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menubar2.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Mad", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Instillinger", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem5 )
		
		self.m_menubar2.Append( self.m_menu2, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.close, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.mad, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.indstil, id = self.m_menuItem5.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()
	
	def mad( self, event ):
		event.Skip()
	
	def indstil( self, event ):
		event.Skip()
	

###########################################################################
## Class MadFrame
###########################################################################

class MadFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bestilling", pos = wx.Point( 100,100 ), size = wx.Size( 500,289 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.nametxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.nametxt.SetToolTipString( u"Navn" )
		
		bSizer3.Add( self.nametxt, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Pizza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.pizzaPris = wx.StaticText( self, wx.ID_ANY, u"45,- kr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pizzaPris.Wrap( -1 )
		gSizer1.Add( self.pizzaPris, 0, wx.ALL, 5 )
		
		pizza_choiceChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.pizza_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pizza_choiceChoices, 0 )
		self.pizza_choice.SetSelection( 0 )
		gSizer1.Add( self.pizza_choice, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Burger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.burgerPris = wx.StaticText( self, wx.ID_ANY, u"45,- kr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.burgerPris.Wrap( -1 )
		gSizer1.Add( self.burgerPris, 0, wx.ALL, 5 )
		
		burger_choiceChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.burger_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, burger_choiceChoices, 0 )
		self.burger_choice.SetSelection( 0 )
		gSizer1.Add( self.burger_choice, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Cola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.colaPris = wx.StaticText( self, wx.ID_ANY, u"12,- kr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.colaPris.Wrap( -1 )
		gSizer1.Add( self.colaPris, 0, wx.ALL, 5 )
		
		cola_choiceChoices = [ u"0", u"1", u"2", u"3", u"4", u"5" ]
		self.cola_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cola_choiceChoices, 0 )
		self.cola_choice.SetSelection( 0 )
		gSizer1.Add( self.cola_choice, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Samlet pris:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.label_ialt = wx.StaticText( self, wx.ID_ANY, u"ialt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_ialt.Wrap( -1 )
		self.label_ialt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer1.Add( self.label_ialt, 0, wx.ALL, 5 )
		
		self.pris = wx.StaticText( self, wx.ID_ANY, u"0kr.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pris.Wrap( -1 )
		gSizer1.Add( self.pris, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Bestil", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Afslut", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.pizza_choice.Bind( wx.EVT_CHOICE, self.updatePris )
		self.burger_choice.Bind( wx.EVT_CHOICE, self.updatePris )
		self.cola_choice.Bind( wx.EVT_CHOICE, self.updatePris )
		self.m_button1.Bind( wx.EVT_BUTTON, self.bestil )
		self.m_button2.Bind( wx.EVT_BUTTON, self.slut_mad )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def updatePris( self, event ):
		event.Skip()
	
	
	
	def bestil( self, event ):
		event.Skip()
	
	def slut_mad( self, event ):
		event.Skip()
	

###########################################################################
## Class Oversigt_mad
###########################################################################

class Oversigt_mad ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Oversigt over madbestillinger", pos = wx.Point( 800,100 ), size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.bestilling_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer4.Add( self.bestilling_list, 1, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Instillinger
###########################################################################

class Instillinger ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.PrisText = wx.StaticText( self, wx.ID_ANY, u"Priser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PrisText.Wrap( -1 )
		bSizer4.Add( self.PrisText, 0, wx.ALL, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Pizza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.pizzaPris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.pizzaPris, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Burger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.burgerPris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.burgerPris, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Cola", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer2.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.colaPris = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.colaPris, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Gem", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.gem )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def gem( self, event ):
		event.Skip()
	

