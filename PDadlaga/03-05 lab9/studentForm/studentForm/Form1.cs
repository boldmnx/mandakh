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
    public partial class createStudents : Form
    {
        public createStudents()
        {
            InitializeComponent();
        }

        private void save_Click(object sender, EventArgs e)
        {
            ner.Text = nerText.Text;
            nerText.Clear();
            nas.Text = nasText.Text;
            nasText.Clear();
            if (erRadio.Text == "Эр")
            {
                huis.Text =erRadio.Text;
                    }
             if (emRadio.Text == "Эм")
            {
                huisEm.Text =emRadio.Text;
            }
        }

        private void createStudents_Load(object sender, EventArgs e)
        {

        }
    }
}
