VERSION 5.00
Begin VB.Form MyazureApp 
   Caption         =   "自动化程序集合"
   ClientHeight    =   12060
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   20535
   LinkTopic       =   "Form1"
   ScaleHeight     =   12060
   ScaleWidth      =   20535
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command8 
      Caption         =   "|||"
      Height          =   615
      Left            =   19320
      TabIndex        =   12
      Top             =   360
      Width           =   615
   End
   Begin VB.CommandButton Command7 
      Caption         =   "-"
      Height          =   615
      Left            =   18600
      TabIndex        =   11
      Top             =   360
      Width           =   615
   End
   Begin VB.CommandButton Command6 
      Caption         =   "O"
      Height          =   615
      Left            =   17880
      TabIndex        =   10
      Top             =   360
      Width           =   615
   End
   Begin VB.CommandButton Command5 
      Caption         =   "X"
      Height          =   615
      Left            =   17160
      TabIndex        =   9
      Top             =   360
      Width           =   615
   End
   Begin VB.TextBox CommandText 
      Height          =   495
      Left            =   12240
      TabIndex        =   8
      Top             =   11400
      Width           =   8175
   End
   Begin VB.CommandButton Command4 
      Caption         =   "Command4"
      Height          =   495
      Left            =   10320
      TabIndex        =   7
      Top             =   11400
      Width           =   1815
   End
   Begin VB.Frame InfoFrame 
      Caption         =   "Info"
      Height          =   9975
      Left            =   12240
      TabIndex        =   6
      Top             =   1200
      Width           =   8175
      Begin VB.ListBox LogList 
         Height          =   9420
         ItemData        =   "MyazureApp.frx":0000
         Left            =   240
         List            =   "MyazureApp.frx":0007
         TabIndex        =   13
         Top             =   360
         Width           =   7695
      End
   End
   Begin VB.Frame TaskFrame 
      Caption         =   "TaskList"
      Height          =   9855
      Left            =   4440
      TabIndex        =   5
      Top             =   1320
      Width           =   7695
      Begin VB.ListBox TaskList 
         Height          =   7620
         ItemData        =   "MyazureApp.frx":0014
         Left            =   240
         List            =   "MyazureApp.frx":0016
         TabIndex        =   14
         Top             =   360
         Width           =   7215
      End
   End
   Begin VB.Frame ControlPannelFrame 
      Caption         =   "Control"
      Height          =   8055
      Left            =   240
      TabIndex        =   3
      Top             =   3120
      Width           =   3975
      Begin VB.CommandButton Command10 
         Caption         =   "Command1"
         Height          =   495
         Left            =   240
         TabIndex        =   16
         Top             =   1560
         Width           =   3255
      End
      Begin VB.CommandButton Command9 
         Caption         =   "Command1"
         Height          =   495
         Left            =   240
         TabIndex        =   15
         Top             =   960
         Width           =   3255
      End
      Begin VB.CommandButton Command3 
         Caption         =   "Command1"
         Height          =   495
         Left            =   240
         TabIndex        =   4
         Top             =   360
         Width           =   3255
      End
   End
   Begin VB.Frame UserFrame 
      Caption         =   "User"
      Height          =   2895
      Left            =   240
      TabIndex        =   0
      Top             =   120
      Width           =   3975
      Begin VB.TextBox Text3 
         Height          =   375
         Left            =   840
         TabIndex        =   19
         Text            =   "Text2"
         Top             =   960
         Width           =   2655
      End
      Begin VB.TextBox Text2 
         Height          =   375
         Left            =   840
         TabIndex        =   17
         Text            =   "Text2"
         Top             =   480
         Width           =   2655
      End
      Begin VB.CommandButton Command2 
         Caption         =   "Command1"
         Height          =   495
         Left            =   2160
         TabIndex        =   2
         Top             =   2160
         Width           =   1455
      End
      Begin VB.CommandButton Command1 
         Caption         =   "Command1"
         Height          =   495
         Left            =   240
         TabIndex        =   1
         Top             =   2160
         Width           =   1455
      End
      Begin VB.Label Label2 
         Caption         =   "Label1"
         Height          =   375
         Left            =   120
         TabIndex        =   20
         Top             =   960
         Width           =   615
      End
      Begin VB.Label Label1 
         Caption         =   "Label1"
         Height          =   375
         Left            =   120
         TabIndex        =   18
         Top             =   480
         Width           =   615
      End
   End
End
Attribute VB_Name = "MyazureApp"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
