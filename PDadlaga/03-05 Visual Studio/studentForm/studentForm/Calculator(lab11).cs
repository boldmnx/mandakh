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
    public partial class Calculator : Form
    {

        private double number1 = 0;
        private double number2 = 0;
        private string operation = "";
        private double memory = 0;
        public Calculator()
        {
            InitializeComponent();
        }
        double too1, too2;
        int uildel;

        private void btnOne_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "1";
        }

        private void btnTwo_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "2";
        }

        private void btnThree_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "3";
        }

        private void btnFour_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "4";
        }

        private void btnFive_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "5";
        }

        private void btnSix_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "6";
        }

        private void btnSeven_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "7";
        }

        private void btnEight_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "8";
        }

        private void btnNine_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "9";
        }

        private void btnPlus_Click(object sender, EventArgs e)
        {
            number1 = Double.Parse(richTextBox1.Text);
            operation = "+";
            richTextBox1.Text = "";
        }

        private void btnMinus_Click(object sender, EventArgs e)
        {
            number1 = Double.Parse(richTextBox1.Text);
            operation = "-";
            richTextBox1.Text = "";
        }

        private void btnTimes_Click(object sender, EventArgs e)
        {
            number1 = Double.Parse(richTextBox1.Text);
            operation = "*";
            richTextBox1.Text = "";
        }

        private void btnDivision_Click(object sender, EventArgs e)
        {
            number1 = Double.Parse(richTextBox1.Text);
            operation = "/";
            richTextBox1.Text = "";
        }

        private void btnEquals_Click(object sender, EventArgs e)
        {
            number2 = Double.Parse(richTextBox1.Text);
            double result = 0;

            switch (operation)
            {
                case "+":
                    result = number1 + number2;
                    break;
                case "-":
                    result = number1 - number2;
                    break;
                case "*":
                    result = number1 * number2;
                    break;
                case "/":
                    result = number1 / number2;
                    break;
                default:
                    break;
            }

            richTextBox1.Text = result.ToString();
        }

        private void btnC_Click(object sender, EventArgs e)
        {
            number1 = 0;
            number2 = 0;
            operation = "";
            richTextBox1.Text = "";
        }

        private void btnCE_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "";
        }

        private void btnSum_Click(object sender, EventArgs e)
        {
            if (richTextBox1.Text.Length > 0)
            {
                richTextBox1.Text = richTextBox1.Text.Substring(0, richTextBox1.Text.Length - 1);
            }
        }

        private void btnMC_Click(object sender, EventArgs e)
        {
            memory = 0;
        }

        private void btnMR_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = memory.ToString();
        }

        private void btnMS_Click(object sender, EventArgs e)
        {
            memory = Double.Parse(richTextBox1.Text);
            btnMC.Enabled = true;
            btnMR.Enabled = true;
        }

        private void btnMPlus_Click(object sender, EventArgs e)
        {
            memory += Double.Parse(richTextBox1.Text);
            richTextBox1.Clear();
        }

        private void btmMinus_Click(object sender, EventArgs e)
        {
            memory -= Double.Parse(richTextBox1.Text);
        }

        private void btnSquareRoot_Click(object sender, EventArgs e)
        {
            double number = Double.Parse(richTextBox1.Text);
            double result = Math.Sqrt(number);
            richTextBox1.Text = result.ToString();
        }

        private void btnPlusMinus_Click(object sender, EventArgs e)
        {
            double number = Double.Parse(richTextBox1.Text);
            double result = -1 * number;
            richTextBox1.Text = result.ToString();
        }

        private void btnPercent_Click(object sender, EventArgs e)
        {
            double number = Double.Parse(richTextBox1.Text);
            double result = number / 100;
            richTextBox1.Text = result.ToString();
        }

        private void btnOneX_Click(object sender, EventArgs e)
        {
            double number = Double.Parse(richTextBox1.Text);
            double result = 1 / number;
            richTextBox1.Text = result.ToString();
        }

        private void btnDot_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ".";
        }

        private void btnZero_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "0";
        }

        private void BolderdeneCalculator_Load(object sender, EventArgs e)
        {

        }
    }
}
