from abc import ABC
from abc import abstractmethod


class ReportProcessor(ABC):
    def generate_report(self) -> None:
        self.collect_data()
        self.analyze_data()
        self.format_report()
        self.save_report()
        self.send_notification()

    @abstractmethod
    def collect_data(self) -> None:
        pass

    @abstractmethod
    def analyze_data(self) -> None:
        pass

    @abstractmethod
    def format_report(self) -> None:
        pass

    @abstractmethod
    def save_report(self) -> None:
        pass

    def send_notification(self) -> None:
        """Hook Method to send notifications"""

        pass


class SalesReportProcessor(ReportProcessor):
    def collect_data(self) -> None:
        print("Collect Sales Data")

    def analyze_data(self) -> None:
        print("Analyze Sales Data")

    def format_report(self) -> None:
        print("Format Sales Data")

    def save_report(self) -> None:
        print("Save Sales Data")

    def send_notification(self) -> None:
        print("Send Sales Data")


class InventoryReportProcessor(ReportProcessor):
    def collect_data(self) -> None:
        print("Collect Inventory Data")

    def analyze_data(self) -> None:
        print("Analyze Inventory Data")

    def format_report(self) -> None:
        print("Format Inventory Data")

    def save_report(self) -> None:
        print("Save Inventory Data")

    def send_notification(self) -> None:
        print("Send Inventory Data")
