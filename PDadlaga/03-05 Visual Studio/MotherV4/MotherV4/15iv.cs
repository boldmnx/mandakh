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
    public partial class _15iv : Form
    {
        public _15iv()
        {
            InitializeComponent();
        }
        Boolean aldaa = false;

        public void fillTenkhim()
        {
            cmbTenkhim.Items.Add("[Choose]");
            cmbTenkhim.Items.Add("Infomation Technology");
            cmbTenkhim.Items.Add("Accountent");
            cmbTenkhim.Items.Add("Forgien Language");
            cmbTenkhim.Items.Add("Bussiness");
            cmbTenkhim.SelectedIndex = 0;
        }
        public void fillMergejil()
        {
            cmbMergejil.Items.Add("[Choose]");
            cmbMergejil.Items.Add("Accountent-Audit");
            cmbMergejil.Items.Add("Accountent-IT");
            cmbMergejil.Items.Add("Software Developement");
            cmbMergejil.Items.Add("accountent-english");
            cmbMergejil.Items.Add("Information Technology");
            cmbMergejil.Items.Add("accountent-bank");
            cmbMergejil.Items.Add("accountent-taxes");
            cmbMergejil.SelectedIndex = 0;
        }
        public void fillkurs()
        {
            cmbKurs.Items.Add("1st year");
            cmbKurs.Items.Add("2nd year");
            cmbKurs.Items.Add("3rd year");
            cmbKurs.Items.Add("4th year");
            cmbKurs.Items.Add("5th year");
            cmbKurs.SelectedIndex = 0;
        }
        public void filldata()
        {
            dataGridView1.ColumnCount = 12;
            dataGridView1.Columns[0].Name = "Оюутны код";
            dataGridView1.Columns[1].Name = "Овог";
            dataGridView1.Columns[2].Name = "Нэр";
            dataGridView1.Columns[3].Name = "Регистр";
            dataGridView1.Columns[4].Name = "Нас";
            dataGridView1.Columns[5].Name = "Хүйс";
            dataGridView1.Columns[6].Name = "Хаяг";
            dataGridView1.Columns[7].Name = "Тэнхим";
            dataGridView1.Columns[8].Name = "Мэргэжил";
            dataGridView1.Columns[9].Name = "Курс";
            dataGridView1.Columns[10].Name = "Элссэн огноо";
            dataGridView1.Columns[11].Name = "Зураг";
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void maskedTextBox2_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {

        }

        
        private void cmbTenkhim_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
     

        private void cmbMergejil_SelectedIndexChanged(object sender, EventArgs e)
        {
          
        }

        private void cmbKurs_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            
        }

        private void save_Click(object sender, EventArgs e)
        {
            if(maskStCode.Text.Length<8)
            {
                aldaa = true;
                errorCode.SetError(maskStCode, "Оюутны код 8 урттай байх ёстой!");
            }
            if(picZurag.Image==null)
            { aldaa = true;
                errorZurag.SetError(picZurag, "Зураг оруул!");
            }
            if(cmbTenkhim.SelectedIndex==0)
            { aldaa = true;
                errorTenkhim.SetError(cmbTenkhim, "Тэнхим сонгоно уу!");
            }
            if(rbFemale.Checked==false && rbMale.Checked==false)
            { aldaa = true;
                errorHuis.SetError(rbFemale, "Хүйсээ сонгоно уу!");
            }
            if(aldaa==false)
            {
                //DataGridview
                string[] row = new string[]
                {
                    maskStCode.Text,
                    txtOvog.Text,
                    maskRegistr.Text,
                    numUDNas.Value.ToString(),
                    rbMale.Checked == true? "Эр" : "Эм",
                    richAddress.Text,
                    cmbTenkhim.SelectedItem.ToString(),
                    cmbMergejil.SelectedItem.ToString(),
                    cmbKurs.SelectedItem.ToString(),
                    dataElssenOgnoo.Value.ToString(),
                    picZurag.ImageLocation
                };
                dataGridView1.Rows.Add(row);
            }


        }

        private void _15iv_Load(object sender, EventArgs e)
        {
            fillMergejil();
            fillTenkhim();
            fillkurs();
            filldata();
        }

        private void picsel_Click(object sender, EventArgs e)
        {
            OpenFileDialog open = new OpenFileDialog();
            open.Title = "Enter Picture";
            open.Filter = "Image Files (*.jpg, *jpeg, *.png) | *.jpg; *.jpeg; *.png";
            if (open.ShowDialog() == DialogResult.OK)
            {
                picZurag.ImageLocation = open.FileName;
                aldaa = false;
                errorZurag.Clear();
            }
        }
    }
}
