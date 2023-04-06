using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace studentForm
{
    public partial class horwuulegch : Form
    {
        public horwuulegch()
        {
            InitializeComponent();
        }

        private void studentValues_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            double minut, secund, tsag;
            if (textBox2.Text != "")
            {
                tsag = Convert.ToDouble(textBox1.Text);
                minut = tsag * 60;
                secund = tsag * 3600;
                label11.Text = minut.ToString();
                label12.Text = secund.ToString();
            }
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            double jil, sar, udur;
            if (textBox1.Text != "")
            {
                jil = Convert.ToDouble(textBox1.Text);
                sar = jil * 12;
                udur = sar * 365;
                label4.Text = sar.ToString();
                label5.Text = udur.ToString();
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            double tugrug, dollar, yuan;
            if (textBox3.Text != "")
            {
                tugrug = Convert.ToDouble(textBox3.Text);
                dollar = tugrug / 3500;
                yuan = tugrug / 510;
                label20.Text = dollar.ToString();
                label21.Text = yuan.ToString();
            }


        }

        private void label30_Click(object sender, EventArgs e)
        {

        }

        private void label23_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            double cells, fah;
            if (textBox4.Text != "")
            {
                cells = Convert.ToDouble(textBox4.Text);
                fah = (cells * 9 / 5) + 32;
                label28.Text = fah.ToString();
            }

        }

        private void label24_Click(object sender, EventArgs e)
        {

        }

        private void label25_Click(object sender, EventArgs e)
        {

        }

        private void label26_Click(object sender, EventArgs e)
        {

        }

        private void label27_Click(object sender, EventArgs e)
        {

        }

        private void label28_Click(object sender, EventArgs e)
        {

        }

        private void label29_Click(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void label22_Click(object sender, EventArgs e)
        {

        }
    }
}
