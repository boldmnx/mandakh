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
    public partial class Notepad_lab13_ : Form
    {
        public Notepad_lab13_()
        {
            InitializeComponent();
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ChildNotepad childNotepad = new ChildNotepad();
            childNotepad.MdiParent = this;
            childNotepad.Show();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
           this.Close();

        }
        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Title = "Save Filee";
            saveFileDialog.Filter = "Text Document. (*.txt|*.txt|All files|*.*)";
            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
                r.SaveFile(saveFileDialog.FileName, RichTextBoxStreamType.UnicodePlainText);
            }
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog o = new OpenFileDialog();
            o.Title = "Open Filee";
            o.Filter = "Text Document. (*.txt|*.txt)";
            if (o.ShowDialog() == DialogResult.OK)
            {
                ChildNotepad childNotepad = new ChildNotepad();
                childNotepad.Parent = this;
                childNotepad.Show();
                RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
                r.LoadFile(o.FileName, RichTextBoxStreamType.UnicodePlainText);
            }
        }

        private void editToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Undo();
        }

        private void cutToolStripMenuItem_Click(object sender, EventArgs e)
        {

            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Cut();
        }

        private void copyToolStripMenuItem_Click(object sender, EventArgs e)
        {

            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Copy();
        }

        private void pastToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Paste();
        }

        private void selectAllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.SelectAll();
        }

        private void undoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Undo();
        }

        private void redoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            RichTextBox r = (RichTextBox)(this.ActiveMdiChild.Controls[0]);
            r.Redo();
        }

        private void pageSetupToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PageSetup pageSetup = new PageSetup();
            pageSetup.MdiParent = this;
            pageSetup.Show();
        }

        private void fontToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Fonts fonts = new Fonts();
            fonts.MdiParent = this;
            fonts.Show();
        }

       
    }
}
