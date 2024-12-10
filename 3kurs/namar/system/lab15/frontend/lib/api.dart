import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  final String baseUrl = "http://127.0.0.1:8000"; // API base URL

  // Fetch the list of students from the backend
  Future<List<Student>> getStudents() async {
    final response = await http.get(Uri.parse('$baseUrl/students/'));

    if (response.statusCode == 200) {
      List data = json.decode(utf8.decode(response.bodyBytes));
      return data.map((json) => Student.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load students');
    }
  }

  Future<void> createStudent(Student student) async {
    final response = await http.post(
      Uri.parse('$baseUrl/students/'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'stfname': student.stName,
        'stlname': student.stOvog,
        'stcode': student.stCode,
        'address': student.geriinHayg,
        'born': student.ognoo,
      }),
    );

    if (response.statusCode == 201) {
      print('Оюутан амжилттай нэмэгдлээ');
    } else {
      throw Exception('Оюутан нэмхэд алдаа гарлаа');
    }
  }

  Future<void> updateStudent(Student student) async {
    final response = await http.put(
      Uri.parse('$baseUrl/students/${student.id}/'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'stlname': student.stOvog,
        'stfname': student.stName,
        'stcode': student.stCode,
        'address': student.geriinHayg,
        'born': student.ognoo,
      }),
    );

    if (response.statusCode == 200) {
      print('Амжилттай заслаа');
    } else {
      throw Exception('Засвар хийхэд алдаа гарлаа');
    }
  }

  Future<void> deleteStudent(int studentId) async {
    final response = await http.delete(
      Uri.parse('$baseUrl/students/$studentId/'),
    );

    print('Амжилттай устгалаа $response');
    // if (response.statusCode == 200) {
    // } else {
    //   print('Алдаа гарлаа: ${response.body}');
    //   throw Exception('Устгаж чадсангүйдээ бро');
    // }
  }
}

class Student {
  final int id;
  final String stName;
  final String? stOvog;
  final String? stCode;
  final String? geriinHayg;
  final String? ognoo;

  Student({
    required this.id,
    required this.stName,
    this.stOvog,
    this.stCode,
    this.geriinHayg,
    this.ognoo,
  });

  // Factory constructor to create a Student from JSON
  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      id: json['id'],
      stName: json['stfname'],
      stOvog: json['stlname'],
      stCode: json['stcode'],
      geriinHayg: json['address'],
      ognoo: json['born'],
    );
  }

  // Method to convert a Student object to JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'stfname': stName,
      'stlname': stOvog,
      'stcode': stCode,
      'address': geriinHayg,
      'born': ognoo,
    };
  }
}
