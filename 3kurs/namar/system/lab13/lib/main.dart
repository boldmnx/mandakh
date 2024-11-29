import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ProfileScreen(),
    );
  }
}

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  final TextEditingController _nameControllerphone = TextEditingController();
  final TextEditingController _nameController = TextEditingController();
  bool _isAgreed = false;
  String _selectedGender = 'Эмэгтэй';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text('Лаб 13'),
          backgroundColor: const Color.fromARGB(255, 68, 39, 218)),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            CircleAvatar(
              radius: 50,
              backgroundImage: AssetImage(
                  'assets/2.jpg'), // Энд өөр зурагны URL ашиглаж болно
            ),
            SizedBox(height: 10),
            Text(
              'Bold-Erdene',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            Text(
              'sw22d046@mandakh.edu.mn',
              style: TextStyle(color: Colors.grey),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.phone, color: Colors.green),
                SizedBox(width: 8),
                Expanded(
                  child: TextField(
                    controller: _nameControllerphone,
                    decoration: InputDecoration(
                      labelText: '8***XXXX',
                    ),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.location_on, color: Colors.green),
                SizedBox(width: 8),
                Expanded(
                  child: TextField(
                    controller: _nameController,
                    decoration: InputDecoration(
                      labelText: 'Монгол улс, Улаанбаатар хот',
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(height: 20),
            Row(
              children: [
                SizedBox(
                  child: ElevatedButton(
                    onPressed: () {
                      // Submit товчлуурын үйлдэл энд байна.
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue, // Товчны дэвсгэр өнгө
                      foregroundColor: Colors.white, // Текстийн өнгө
                      padding:
                          EdgeInsets.symmetric(vertical: 15), // Дээд/доод зай
                      shape: RoundedRectangleBorder(
                        borderRadius:
                            BorderRadius.circular(12), // Хурц өнцөгтэй тохиргоо
                      ),
                    ),
                    child: Text('Засах'),
                  ),
                ),
                SizedBox(
                  child: ElevatedButton(
                    onPressed: () {
                      // Submit товчлуурын үйлдэл энд байна.
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue, // Товчны дэвсгэр өнгө
                      foregroundColor: Colors.white, // Текстийн өнгө
                      padding:
                          EdgeInsets.symmetric(vertical: 15), // Дээд/доод зай
                      shape: RoundedRectangleBorder(
                        borderRadius:
                            BorderRadius.circular(12), // Хурц өнцөгтэй тохиргоо
                      ),
                    ),
                    child: Text('Засах'),
                  ),
                ),
              ],
            ),
            SizedBox(height: 20),
            TextField(
              controller: _nameController,
              decoration: InputDecoration(
                labelText: 'Та нэрээ бичнэ үү',
              ),
            ),
            SizedBox(height: 20),
            TextField(
              controller: _nameController,
              decoration: InputDecoration(
                labelText: 'И-мэйл хаяг',
              ),
            ),
            SizedBox(height: 20),
            CheckboxListTile(
              title: Text('Зөвшөөрөх үү...'),
              value: _isAgreed,
              onChanged: (value) {
                setState(() {
                  _isAgreed = value!;
                });
              },
            ),
            SizedBox(height: 20),
            Row(
              children: [
                Expanded(
                  child: RadioListTile(
                    title: Text('Эмэгтэй'),
                    value: 'Эмэгтэй',
                    groupValue: _selectedGender,
                    onChanged: (value) {
                      setState(() {
                        _selectedGender = value.toString();
                      });
                    },
                  ),
                ),
                Expanded(
                  child: RadioListTile(
                    title: Text('Эрэгтэй'),
                    value: 'Эрэгтэй',
                    groupValue: _selectedGender,
                    onChanged: (value) {
                      setState(() {
                        _selectedGender = value.toString();
                      });
                    },
                  ),
                ),
              ],
            ),
            SizedBox(height: 20),
            SizedBox(
              width: double.infinity, // Товчийг дэлгэцийн өргөнд тохируулах
              child: ElevatedButton(
                onPressed: () {
                  // Submit товчлуурын үйлдэл энд байна.
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color.fromARGB(
                      255, 98, 15, 181), // Товчны дэвсгэр өнгө
                  foregroundColor: Colors.white, // Текстийн өнгө
                  padding: EdgeInsets.symmetric(vertical: 15), // Дээд/доод зай
                  shape: RoundedRectangleBorder(
                    borderRadius:
                        BorderRadius.circular(0), // Хурц өнцөгтэй тохиргоо
                  ),
                ),
                child: Text('Submit'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
