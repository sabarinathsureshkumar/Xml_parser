from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import logging
import sys

import lib_Widgets
import lib_xml_Parser

logging.basicConfig\
    (filename='Arxml_data_extractor.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def browse_files():
    lib_Widgets.main_window.filepath = \
        filedialog.askopenfilename(title="Selectarxml file", filetypes=(("xml files", "*.xml"), ("all files", "*.*")))
    lib_Widgets.CreateTextbox(row='100', column='20', text=lib_Widgets.main_window.filepath, width='50')
    logging.debug('Input File Path: %s', lib_Widgets.main_window.filepath)


def browse_folderpath():
    lib_Widgets.main_window.folderpath = filedialog.askdirectory()
    lib_Widgets.CreateTextbox(row='5000', column='20', text=lib_Widgets.main_window.folderpath, width='50')
    logging.debug('Output folder Path: %s', lib_Widgets.main_window.folderpath)


def generate():
    try:
        parser = lib_xml_Parser.ParseClass(lib_Widgets.main_window.filepath)
        cont_data, subcont_data = parser.extract_cont()
        logging.info('Container Data:%s', cont_data)
        logging.info('Sub-Container Data:%s', subcont_data)
        df1 = pd.DataFrame(cont_data, columns=["Containers_SubContainers - ShortName", "Definition-Ref"])
        df2 = pd.DataFrame(subcont_data, columns=["Containers_SubContainers - ShortName", "Definition-Ref"])
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        out_excel = lib_Widgets.main_window.folderpath + '\ARXML_Extract' + str_current_datetime+'.xlsx'
        writer = pd.ExcelWriter(out_excel, engine='openpyxl')
        df1.to_excel(writer, sheet_name='Container_Data', index=False)
        df2.to_excel(writer, sheet_name='SubContainer_Data', index=False)
        writer.close()
        messagebox.showinfo("Info", "Data extraction from Arxml successful")

    except Exception as e:
        messagebox.showerror("Error", "Please check if .arxml file and the output folder are selected")
        logging.error('Input Missing -  arxml file path or Output folder path')


def close_window():
    lib_Widgets.main_window.quit()
    logging.info('Application closed successfully')


if __name__ == '__main__':
    try:
        parser = lib_xml_Parser.ParseClass(sys.argv[1])
        cont_data, subcont_data = parser.extract_cont()
        logging.info('Container Data:%s', cont_data)
        logging.info('Sub-Container Data:%s', subcont_data)
        df1 = pd.DataFrame(cont_data, columns=["Containers_SubContainers - ShortName", "Definition-Ref"])
        df2 = pd.DataFrame(subcont_data, columns=["Containers_SubContainers - ShortName", "Definition-Ref"])
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        out_excel = sys.argv[2] + '\ARXML_Extract' + str_current_datetime + '.xlsx'
        writer = pd.ExcelWriter(out_excel, engine='openpyxl')
        df1.to_excel(writer, sheet_name='first_sheet', index=False)
        df2.to_excel(writer, sheet_name='second_sheet', index=False)
        writer.close()

    except:
        obj = lib_Widgets.CreateWidget\
            (widget_type='MainWindow', title='Autosar xml Parser', iconimg='tool_icon.bmp',
             geometry='800x110', bg='lightblue')
        main_window = obj.create_mainwindow()
        label1 = lib_Widgets.CreateLabel(text='Autosar xml File', row='100', bg='lightblue')
        input_label1 = label1.create_inputlabel()
        label2 = lib_Widgets.CreateLabel(text='Output File Path', row='5000', bg='lightblue')
        input_label2 = label2.create_inputlabel()
        text1 = lib_Widgets.CreateTextbox(row='100', column='20', text='', width='50')
        text2 = lib_Widgets.CreateTextbox(row='5000', column='20', text='', width='50')
        browse_button1 = lib_Widgets.CreateButtons(text='    Browse    ', command=browse_files, row=675, column=1)
        act_button1 = browse_button1.create_button()
        browse_button2 = lib_Widgets.CreateButtons(text='    Browse    ', command=browse_folderpath, row=675, column=30)
        act_button2 = browse_button2.create_button()
        generate_button = lib_Widgets.CreateButtons(text='  Generate  ', command=generate, row=300, column=70)
        act_button3 = generate_button.create_button()
        exit_button = lib_Widgets.CreateButtons(text='  Exit  ', command=close_window, row=400, column=70)
        act_button4 = exit_button.create_button()

        lib_Widgets.main_window.mainloop()
