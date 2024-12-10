import 'package:flutter/material.dart';
import 'api.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: StudentPage(),
    );
  }
}

class StudentPage extends StatefulWidget {
  @override
  _StudentPageState createState() => _StudentPageState();
}

class _StudentPageState extends State<StudentPage> {
  late ApiService apiService;
  late Future<List<Student>> students;

  @override
  void initState() {
    super.initState();
    apiService = ApiService();
    students = apiService.getStudents();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Оюутан')),
      body: FutureBuilder<List<Student>>(
        future: students,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Алдаа: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('Оюутан олдсонгүй'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                final student = snapshot.data![index];
                return ListTile(
                  title: Text(student.stName),
                  subtitle: Text(
                    student.stOvog ?? '',
                  ),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      IconButton(
                        icon: Icon(Icons.edit),
                        onPressed: () async {
                          final updatedStudent = await Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => StudentForm(
                                student: student,
                              ),
                            ),
                          );

                          if (updatedStudent != null) {
                            await apiService.updateStudent(updatedStudent);
                            setState(() {
                              students = apiService.getStudents(); // Refresh
                            });
                          }
                        },
                      ),
                      IconButton(
                        icon: Icon(Icons.delete),
                        onPressed: () async {
                          await apiService.deleteStudent(student.id);
                          setState(() {
                            students = apiService.getStudents(); // Refresh
                          });
                        },
                      ),
                    ],
                  ),
                );
              },
            );
          }
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          final newStudent = await Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => StudentForm()),
          );

          if (newStudent != null) {
            await apiService.createStudent(newStudent);
            setState(() {
              students = apiService.getStudents(); // Refresh
            });
          }
        },
        child: Icon(Icons.add),
      ),
    );
  }
}

class StudentForm extends StatefulWidget {
  final Student? student;

  const StudentForm({this.student});

  @override
  _StudentFormState createState() => _StudentFormState();
}

class _StudentFormState extends State<StudentForm> {
  final _formKey = GlobalKey<FormState>();
  late String stName, stOvog, stCode, geriinHayg, ognoo;

  @override
  void initState() {
    super.initState();
    stName = widget.student?.stName ?? '';
    stOvog = widget.student?.stOvog ?? '';
    stCode = widget.student?.stCode ?? '';
    geriinHayg = widget.student?.geriinHayg ?? '';
    ognoo = widget.student?.ognoo ?? '';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.student == null ? 'Add Student' : 'Edit Student'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              _buildTextField(
                'First Name',
                stName,
                (value) => stName = value,
              ),
              _buildTextField('Last Name', stOvog, (value) => stOvog = value),
              _buildTextField('Code', stCode, (value) => stCode = value),
              _buildTextField(
                  'Address', geriinHayg, (value) => geriinHayg = value),
              _buildTextField('Born', ognoo, (value) => ognoo = value),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    Navigator.pop(
                      context,
                      Student(
                        id: widget.student?.id ?? 0,
                        stName: stName,
                        stOvog: stOvog,
                        stCode: stCode,
                        geriinHayg: geriinHayg,
                        ognoo: ognoo,
                      ),
                    );
                  }
                },
                child: Text('Save'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTextField(
      String label, String? initialValue, Function(String) onChanged) {
    return TextFormField(
      initialValue: initialValue,
      decoration: InputDecoration(labelText: label),
      onChanged: onChanged,
      validator: (value) => value!.isEmpty ? '$label is required' : null,
    );
  }
}
