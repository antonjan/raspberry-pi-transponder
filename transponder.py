import os
import time
from gnuradio import gr
from gnuradio import blocks
from gnuradio import analog
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import uhd

# Configure the RTL-SDR source
rtl_sdr_source = uhd.usrp_source(
    ",".join(("", "")),
    uhd.stream_args(
        cpu_format="fc32",
        otw_format="sc8",
        args="addr=0",
    ),
)

rtl_sdr_source.set_samp_rate(2e6)  # Sample rate (2 MHz)
rtl_sdr_source.set_center_freq(435.1e6)  # Center frequency (435.1 MHz)
rtl_sdr_source.set_gain(20)  # Set an appropriate gain value

# Configure the rpitx sink
rpitx_sink = os.popen('sudo rpitx -m RF -i <(csdr convert_f_s16 | csdr realpart_s16_to_c8) -f 145950000')

# Create the flow graph
class flow_graph(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        # Connect the RTL-SDR source to the rpitx sink
        self.connect((rtl_sdr_source, 0), (rpitx_sink, 0))

if __name__ == '__main__':
    try:
        tb = flow_graph()
        tb.start()
        tb.wait()
    except KeyboardInterrupt:
        pass
    finally:
        tb.stop()
