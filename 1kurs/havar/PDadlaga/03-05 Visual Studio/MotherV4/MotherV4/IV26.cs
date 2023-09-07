using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MotherV4
{
    public partial class IV26 : Form
    {
        public IV26()
        {
            InitializeComponent();
        }

        private void IV26_Load(object sender, EventArgs e)
        {

        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            timer1.Interval = trackBar1.Value * 200;
        }

        private void picplay_Click(object sender, EventArgs e)
        {
            timer1.Start();
        }

        private void picadd_Click(object sender, EventArgs e)
        {
            OpenFileDialog open = new OpenFileDialog();
            open.Title = "Enter Picture File";
            open.Filter = "Picture Files (*.jpg, *.jpeg, *.png) | *.jpg; *.jpeg; *.png";
            if (open.ShowDialog() == DialogResult.OK)
            {
                listBox1.Items.AddRange(open.FileNames);
            }
        }

        private void picremov_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            if (listBox1.SelectedIndex != -1 && listBox1.Items.Count !=0)
            {
                listBox1.Items.RemoveAt(listBox1.SelectedIndex);
            }
        }

        private void picclear_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            listBox1.Items.Clear();
            picslide.Image = null;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex != -1)
            {
                picslide.ImageLocation = listBox1.SelectedItem.ToString();
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == listBox1.Items.Count -1)
            {
                listBox1.SetSelected(0, true);
            }
            else
            {
                listBox1.SetSelected(listBox1.SelectedIndex + 1, true);
            }
        }

        private void picpause_Click(object sender, EventArgs e)
        {
            timer1.Stop();
        }

        private void picfirst_Click(object sender, EventArgs e)
        {
            listBox1.SetSelected(0, true);
        }

        private void pipcprev_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == 0)
            { listBox1.SetSelected(listBox1.Items.Count - 1, true);  }
            else
            {
                listBox1.SetSelected(listBox1.SelectedIndex - 1, true);
            }
        }

        private void picnext_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == listBox1.Items.Count -1)
            { listBox1.SetSelected(0, true); }
            else
            {
                listBox1.SetSelected(listBox1.SelectedIndex + 1, true);
            }
        }

        private void piclast_Click(object sender, EventArgs e)
        {
            listBox1.SetSelected(listBox1.Items.Count - 1, true);
        }
    }
}
