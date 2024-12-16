import os
import sys
import enum
import logging
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDateEdit, QPushButton, QFileDialog
from PyQt6.QtCore import Qt, QDate
from datetime import datetime

# Настройка логирования
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

sys.path.insert(0, "C:/Users/pudov/Desktop/lab3/Lab2")

from get_value_form_date import read_data_for_date
from spliting_into_two_files import split_csv_by_columns
from division_by_year import split_csv_by_years
from division_by_week import split_csv_by_weeks


class Mode(enum.Enum):
    split_csv_by_weeks = 3
    split_csv_by_year = 2
    split_by_x_y = 1


class DateApp(QWidget):
    def __init__(self):
        """
        Initialize the DateApp widget.
        """
        super().__init__()

        self.data_path = None

        self.date_label = QLabel('Select date:')
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())  # Set the current date by default

        self.browse_data_button = QPushButton('Browse Data', self)
        self.browse_data_button.clicked.connect(self.browse_data)

        self.split_button = QPushButton('Split Data', self)
        self.split_button.clicked.connect(lambda: self.file_splitter(Mode.split_by_x_y))

        self.split_by_year_button = QPushButton('Split by year', self)
        self.split_by_year_button.clicked.connect(lambda: self.file_splitter(Mode.split_csv_by_year))

        self.split_by_week_button = QPushButton('Split by week', self)
        self.split_by_week_button.clicked.connect(lambda: self.file_splitter(Mode.split_csv_by_weeks))

        self.select_datafile = QLabel('No data file selected')

        self.result_label = QLabel('Data for the selected date will be displayed here')

        self.get_data_button = QPushButton('Get Data')
        self.get_data_button.clicked.connect(self.show_data)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)
        layout.addWidget(self.browse_data_button)
        layout.addWidget(self.select_datafile)
        layout.addWidget(self.get_data_button)
        layout.addWidget(self.split_button)
        layout.addWidget(self.split_by_week_button)
        layout.addWidget(self.split_by_year_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.setWindowTitle('GetDataByDate')
        self.setGeometry(300, 300, 400, 200)

    def browse_data(self) -> None:
        """
        Open file dialog to select a data file.
        """
        self.data_path, _ = QFileDialog.getOpenFileName(self, "Select Data File")
        if self.data_path:
            self.select_datafile.setText(os.path.basename(self.data_path))
            logging.info(f"Data file selected: {self.data_path}")
        else:
            logging.warning("No data file selected.")

    def show_data(self) -> None:
        """
        Display data for the selected date.
        """
        selected_date = self.date_edit.date().toString(Qt.DateFormat.ISODate)
        if self.data_path is not None:
            r = read_data_for_date(file_path=self.data_path,
                                   target_date=datetime.strptime(selected_date, '%Y-%m-%d'))
            if r is not None:
                self.result_label.setText(" ".join(r))
                logging.info(f"Data retrieved for date: {selected_date}")
            else:
                self.result_label.setText("No data for the selected time")
                logging.warning(f"No data found for date: {selected_date}")
        else:
            self.result_label.setText("Please select a file")
            logging.error("Attempted to retrieve data without selecting a file.")

    def file_splitter(self, mode: Mode) -> None:
        """
        Splitting into files
        """
        if self.data_path is not None:
            if mode == Mode.split_by_x_y:
                success = split_csv_by_columns(input_file=self.data_path,
                                                output_file_x=f'{os.path.dirname(self.data_path)}/X.csv',
                                                output_file_y=f'{os.path.dirname(self.data_path)}/Y.csv')
                if success:
                    self.result_label.setText("Files created successfully")
                    logging.info("Data split into X and Y files successfully.")
                else:
                    logging.error("Failed to split data into X and Y files.")

            elif mode == Mode.split_csv_by_year:
                success = split_csv_by_years(input_file=self.data_path,
                                              output_folder=f'{os.path.dirname(self.data_path)}/years')
                if success:
                    self.result_label.setText("Files created successfully")
                    logging.info("Data split by year successfully.")
                else:
                    logging.error("Failed to split data by year.")

            elif mode == Mode.split_csv_by_weeks:
                success = split_csv_by_weeks(input_file=self.data_path,
                                              output_folder=f'{os.path.dirname(self.data_path)}/weeks')
                if success:
                    self.result_label.setText("Files created successfully")
                    logging.info("Data split by week successfully.")
                else:
                    logging.error("Failed to split data by week.")
        else:
            logging.error("Attempted to split data without selecting a file.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DateApp()
    window.show()
    sys.exit(app.exec())