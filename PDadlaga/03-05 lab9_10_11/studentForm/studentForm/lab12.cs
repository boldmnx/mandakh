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
    public partial class lab12 : Form
    {
        Boolean isDragging = false;
        int currentX, currentY;
        public lab12()
        {
            InitializeComponent();
            textBox1.Text = "Энэ хэсэгт тегст оруул!";
            textBox1.ForeColor = SystemColors.GrayText;
        }

      
        private void button1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                button1.Height += 10;
                button1.Width += 10;
                button1.BackColor = Color.Yellow;
                button1.Text = "Left Click";
            }
            else if (e.Button == MouseButtons.Right)
            {
                button1.Height -= 10;
                button1.Width -= 10;
                button1.BackColor = Color.Orange;
                button1.Text = "Right Click";
            }
        }

        private void button2_MouseDown(object sender, MouseEventArgs e)
        {
            isDragging = true;
            currentX = e.X;
            currentY = e.Y;
        }

        private void button2_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDragging)
            {
                button2.Top = button2.Top + (e.Y - currentY);
                button2.Left = button2.Left + (e.X - currentX);
            }
        }

        private void button2_MouseUp(object sender, MouseEventArgs e)
        {
            isDragging = false;
        }

        private void textBox1_Enter(object sender, EventArgs e)
        {
            if (textBox1.Text == "Энэ хэсэгт тегст оруул!")
            {
                textBox1.Text = "";
                textBox1.ForeColor = SystemColors.WindowText;
            }
        }

        private void textBox1_Leave(object sender, EventArgs e)
        {
            if (textBox1.Text.Length == 0)
            {
                textBox1.Text = "Энэ хэсэгт тегст оруул!";
                textBox1.ForeColor = SystemColors.GrayText;
            }
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsLetter(e.KeyChar) == false && char.IsControl(e.KeyChar) == false)
            {
                e.Handled = true;
            }
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar) == false && char.IsControl(e.KeyChar) == false)
            {
                e.Handled = true;
            }
        }

        private void textBox4_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar) == false)
            {
                e.Handled = true;
            }
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            if (textBox4.Text.Length > 0)
            {
                int i = Convert.ToInt32(textBox4.Text) * 10;
                label1.Text = i.ToString();
            }
        }
    }
}
