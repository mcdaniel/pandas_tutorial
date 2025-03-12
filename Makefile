#
# Makefile - makefile for pandas/matplotlib/seaborn tutorial
# Author: Patrick McDaniel
#

# Environment
MPL_FIGS=	data/mpl_pi_chart.png \
			data/mpl_wordle_freq_bar.png \
			data/mpl_numbers.png \
			data/mpl_complex.png
SNS_FIGS=	data/sns_pi_chart.png \
			data/sns_scatter.png

# Productions

all: $(MPL_FIGS) $(SNS_FIGS)

data/mpl_pi_chart.png: mpl_example1.py
	python mpl_example1.py

data/mpl_wordle_freq_bar.png: mpl_example2.py
	python mpl_example2.py

data/mpl_numbers.png: mpl_example3.py
	python mpl_example3.py

data/mpl_complex.png: mpl_example4.py
	python mpl_example4.py

data/sns_pi_chart.png: sns_example1.py
	python sns_example1.py

data/sns_scatter.png: sns_example2.py
	python sns_example2.py

clean:
	rm -f $(MPL_FIGS) $(SNS_FIGS)