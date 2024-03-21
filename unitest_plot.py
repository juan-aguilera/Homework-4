import unittest
import running_file
import matplotlib.pyplot as plt

class PlotTest(unittest.TestCase):

    def test_Plotting(self):
        test_plot = running_file.plot_execution_time()
        self.assertIsInstance(test_plot, plt.Figure)
        pass

if __name__ == "__main__":
    unittest.main()



