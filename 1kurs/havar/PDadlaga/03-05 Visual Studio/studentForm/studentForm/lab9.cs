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
            string gender;
            ner.Text = nerText.Text;
            nerText.Clear();
            nas.Text = nasText.Text;
            nasText.Clear();
            gender = erRadio.Text;
            gender = emRadio.Text;
            if (erRadio.Checked == true)
            {
                gender = "Эр";
                huis.Text = gender;
            }
            else
            {
                gender = "Эм";
                huisEm.Text = gender;
            }
            label12.Text = mergejil.Text;
            date.Text = dateTimePicker1.Text;
        }

        private void createStudents_Load(object sender, EventArgs e)
        {
            lab12 lab12 = new lab12();
            lab12.ShowDialog();
            //createStudents createStudent = new createStudents();
            //createStudent.Hide();
            //MessageBox.Show("Hello Teacher");
        }

        private void mergejil_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            createStudents createStudents = new createStudents();
            createStudents.Hide();
            horwuulegch horwuulegch = new horwuulegch();
            horwuulegch.ShowDialog();
        }
    }
}
