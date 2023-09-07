using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            maskedRegister.Mask = "LL00000000";
            maskedCode.Mask = "LL00L0000";
            
        }

        private void signUpBtn_Click(object sender, EventArgs e)
        {
            bool hasError = false;
            errorProvider1.Clear();
            errorProvider2.Clear();
            errorProvider3.Clear();
            errorProvider4.Clear();
            errorProvider5.Clear();
            errorProvider6.Clear();
            errorProvider7.Clear();
            errorProvider8.Clear();
            errorProvider9.Clear();
            errorProvider10.Clear();
            errorProvider11.Clear();

            if (Portrait.Image == null)
            {
                errorProvider11.SetError(Portrait, "Picture is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(maskedCode.Text))
            {
                errorProvider11.SetError(maskedCode, "Code is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(Fname.Text))
            {
                errorProvider1.SetError(Fname, "First Name is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(Lname.Text))
            {
                errorProvider2.SetError(Lname, "Last Name is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(Address.Text))
            {
                errorProvider3.SetError(Address, "Address is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(maskedRegister.Text))
            {
                errorProvider4.SetError(maskedRegister, "Register Number is required");
                hasError = true;
            }
            if (string.IsNullOrEmpty(maskedCode.Text))
            {
                errorProvider5.SetError(maskedCode, "Code is required");
                hasError = true;
            }
            if (cmbSchool.SelectedItem == null)
            {
                errorProvider6.SetError(cmbSchool, "School is required");
                hasError = true;
            }
            if (cmbProfession.SelectedItem == null)
            {
                errorProvider7.SetError(cmbProfession, "Profession is required");
                hasError = true;
            }
            if (cmbCourse.SelectedItem == null)
            {
                errorProvider8.SetError(cmbCourse, "Course is required");
                hasError = true;
            }
            if (dateTimePicker1.Value == null)
            {
                errorProvider9.SetError(dateTimePicker1, "Date of Birth is required");
                hasError = true;
            }
            if (!radioBtnMale.Checked && !radioBtnFemale.Checked)
            {
                errorProvider10.SetError(groupBox1, "Gender is required");
                hasError = true;
            }

            if (!hasError)
            {
                string firstName = Fname.Text;
                string lastName = Lname.Text;
                string address = Address.Text;
                string registerNumber = maskedRegister.Text;
                string code = maskedCode.Text;
                string school = cmbSchool.SelectedItem?.ToString();
                string profession = cmbProfession.SelectedItem?.ToString();
                string course = cmbCourse.SelectedItem?.ToString();
                string dateOfBirth = dateTimePicker1.Value.ToShortDateString();
                string gender = radioBtnMale.Checked ? "Male" : "Female";
                int age = (int)numUDNas.Value;

                DataGridViewRow newRow = new DataGridViewRow();
                newRow.CreateCells(dataGridView1);
                newRow.Cells[0].Value = firstName;
                newRow.Cells[1].Value = lastName;
                newRow.Cells[2].Value = address;
                newRow.Cells[3].Value = registerNumber;
                newRow.Cells[4].Value = code;
                newRow.Cells[5].Value = school;
                newRow.Cells[6].Value = profession;
                newRow.Cells[7].Value = course;
                newRow.Cells[8].Value = dateOfBirth;
                newRow.Cells[9].Value = gender;
                newRow.Cells[10].Value = age;
                dataGridView1.Rows.Add(newRow);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.ColumnCount = 11;
            dataGridView1.Columns[0].Name = "First Name";
            dataGridView1.Columns[1].Name = "Last Name";
            dataGridView1.Columns[2].Name = "Address";
            dataGridView1.Columns[3].Name = "Register Number";
            dataGridView1.Columns[4].Name = "Code";
            dataGridView1.Columns[5].Name = "School";
            dataGridView1.Columns[6].Name = "Profession";
            dataGridView1.Columns[7].Name = "Course";
            dataGridView1.Columns[8].Name = "Date of Birth";
            dataGridView1.Columns[9].Name = "Gender";
            dataGridView1.Columns[10].Name = "Age";
        }

        private void addPicBtn_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.Filter = "Image files (*.jpg, *.jpeg, *.png) | *.jpg; *.jpeg; *.png";

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    Portrait.Image = Image.FromFile(openFileDialog.FileName);
                }
            }
        }

        private void clearBtn_Click(object sender, EventArgs e)
        {
            Fname.Text = "";
            Lname.Text = "";
            Address.Text = "";
            maskedRegister.Text = "";
            maskedCode.Text = "";
            cmbSchool.SelectedItem = null;
            cmbProfession.SelectedItem = null;
            cmbCourse.SelectedItem = null;
            dateTimePicker1.Value = DateTime.Now;
            radioBtnMale.Checked = true;
            numUDNas.Value = 18;
            Portrait.Image = null;
            errorProvider1.Clear();
            errorProvider2.Clear();
            errorProvider3.Clear();
            errorProvider4.Clear();
            errorProvider5.Clear();
            errorProvider6.Clear();
            errorProvider7.Clear();
            errorProvider8.Clear();
            errorProvider9.Clear();
            errorProvider10.Clear();
            errorProvider11.Clear();
        }

        private void cmbSchool_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void maskedCode_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {

        }
    }
}
