button_style = '''
        QPushButton {
        font-size: 15px;
        font-weight: 300;
        color: #fff;
        border: 0.3rem solid transparent;
        border-radius: 25;
        background-color: #60605e;
        }
        QPushButton:hover {
        background-color: #787875;
        }
        QPushButton:pressed {
        color: #0F462D;
        background-color: #E4FFDF;
        }
        '''

button_style2 = '''
        QPushButton {
        font-size: 15px;
        font-weight: 300;
        color: #fff;
        border: 0.3rem solid transparent;
        border-radius: 25;
        background-color: #B7E3E4;
        }
        QPushButton:hover {
        background-color: #7DCDCE;
        }
        QPushButton:pressed {
        color: #B7E3E4;
        background-color: #071213;
        }
        '''

logout_button = '''
        QPushButton {
        border-radius: 10;
        font-weight: 700;
        color: #fff;
        border: 0.3rem solid transparent;
        background-color: #2A2A2A45;
        }
        QPushButton:hover {
        background-color: #7DCDCE;
        }
        QPushButton:pressed {
        color: #B7E3E4;
        background-color: #071213;
        }
        '''

form_style = '''
    QLineEdit {
    font-size: 25px;
    font-weight: 100;
    padding-left: 0.4em;
    border-radius: 12.5;
}
'''
form_style2 = '''
    QLineEdit {
    font-size: 15px;
    padding-left: 0.4em;
    border-radius: 12.5;
    background-color: #707070;
    color: #ffffff;
}
'''


alert = "background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;"
success = "background-color: #E4FFDF; color: #0F462D; border-radius:16px"

list_style = '''
        QListWidget{ 
        padding: 10px; 
        border : 1px solid transparent;
        border-radius: 25; 
        background : #1A1A1A;
        font-size: 20px;
        }
        QListWidget QScrollBar{
        background : lightblue
        }
        QListWidget::item{
        background : #454545;
        border-radius: 20;
        padding: 10px;
        margin: 5px;
        }
        QListView::item:selected{ 
        border-radius: 20; 
        background : #E4FFDF;
        color: #0F462D;
        padding: 10px;
}
'''

block_style = '''
    QLabel {
    padding-left: 0.4em;
    border-radius: 12.5;
    font-size: 5em;
    font-weight: 100;
    background-color: #707070;
    color: #ffffff;
}
'''