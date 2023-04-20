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
    public partial class BolderdeneCalculator : Form
    {
        public BolderdeneCalculator()
        {
            InitializeComponent();
        }
        double too1, too2;
        int uildel;

        private void btnOne_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 1;
            txtDisplay.Text = too1.ToString();
        }

        private void btnTwo_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 2;
            txtDisplay.Text = too1.ToString();
        }

        private void btnThree_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 3;
            txtDisplay.Text = too1.ToString();
        }

        private void btnFour_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 4;
            txtDisplay.Text = too1.ToString();
        }

        private void btnFive_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 5;
            txtDisplay.Text = too1.ToString();
        }

        private void btnSix_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 6;
            txtDisplay.Text = too1.ToString();
        }

        private void btnSeven_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 7;
            txtDisplay.Text = too1.ToString();
        }

        private void btnEight_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 8;
            txtDisplay.Text = too1.ToString();
        }

        private void btnNine_Click(object sender, EventArgs e)
        {
            too1 = too1 * 10;
            too1 = too1 + 9;
            txtDisplay.Text = too1.ToString();
        }

        private void btnPlus_Click(object sender, EventArgs e)
        {
            too2 = too1;
            too1 = 0;
            txtDisplay.Text = "0";
            uildel = 1;
        }

        private void btnMinus_Click(object sender, EventArgs e)
        {
            too2 = too1;
            too1 = 0;
            txtDisplay.Text = "0";
            uildel = 2;
        }

        private void btnTimes_Click(object sender, EventArgs e)
        {
            too2 = too1;
            too1 = 0;
            txtDisplay.Text = "0";
            uildel = 3;
        }

        private void btnDivision_Click(object sender, EventArgs e)
        {
            too2 = too1;
            too1 = 0;
            txtDisplay.Text = "0";
            uildel = 4;
        }

        private void btnEquals_Click(object sender, EventArgs e)
        {
            switch (uildel)
            {
                case 1: txtDisplay.Text = (too2 + too1).ToString(); break;
                case 2: txtDisplay.Text = (too2 - too1).ToString(); break;
                case 3: txtDisplay.Text = (too2 * too1).ToString(); break;
                case 4: txtDisplay.Text = (too2 / too1).ToString(); break;
            }
        }

        private void BolderdeneCalculator_Load(object sender, EventArgs e)
        {

        }
    }
}
