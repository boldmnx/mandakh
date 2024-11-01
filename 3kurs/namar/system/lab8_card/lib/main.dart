import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Lab8'),
        ),
        body: Row(
          children: [
            Card(
              elevation: 19,
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15)),
              child: Column(
                children: [Text('Create Account')],
              ),
            )
          ],
        ),
      ),
    );
  }
}
