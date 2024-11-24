import 'package:flutter/material.dart';
import 'package:dotted_border/dotted_border.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Box with Shadow Example'),
        ),
        body: Padding(
          padding: const EdgeInsets.only(left: 30.0, bottom: 100.0, top: 50.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              // Column for large boxes
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  // First large container with shadow
                  Container(
                    width: 200,
                    height: 200,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(15),
                      border: Border(
                        top: BorderSide(color: Colors.green, width: 5),
                        left: BorderSide(color: Colors.green, width: 5),
                        right: BorderSide(color: Colors.green, width: 5),
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.green.withOpacity(0.5),
                          spreadRadius: 5,
                          blurRadius: 7,
                          offset: Offset(0, 3),
                        ),
                      ],
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          'GeeksforGeeks',
                          style: TextStyle(
                            fontSize: 24,
                            color: Colors.green,
                          ),
                          textAlign: TextAlign.center,
                        ),
                        Text(
                          'A computer science portal for geeks',
                          style: TextStyle(
                            fontSize: 8,
                            color: Colors.black,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ],
                    ),
                  ),
                  SizedBox(height: 20), // Space between large boxes
                  // Second large container
                  Stack(
                    children: [
                      DottedBorder(
                        borderType: BorderType.RRect,
                        radius: Radius.circular(12),
                        padding: EdgeInsets.all(6),
                        color:
                            Colors.black, // Set the color for the dotted border
                        strokeWidth: 1, // Adjust stroke width if needed
                        child: ClipRRect(
                          borderRadius: BorderRadius.all(Radius.circular(12)),
                          child: Container(
                            height: 60,
                            width: 200,
                            child: Center(
                              child: Text(
                                'FlutterBeads',
                                style: TextStyle(
                                  fontSize: 24,
                                  color: Colors.black,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      // Overlay a container to cover the right border
                      Positioned(
                        right: -3,
                        top: 0,
                        bottom: 0,
                        width: 10, // Adjust the width to match the border width
                        child: Container(
                          color: Colors.white, // Same as your background color
                        ),
                      ),
                    ],
                  ),
                ],
              ),
              SizedBox(width: 80), // Space between large and small boxes
              // Column for small boxes
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // First small box
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border.all(color: Colors.green, width: 2),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Second small box
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                          left: BorderSide(color: Colors.green, width: 2)),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Third small box with top border
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                          top: BorderSide(color: Colors.green, width: 2)),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Fourth small box with right border
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                          right: BorderSide(color: Colors.green, width: 2)),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Fifth small box with bottom border
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                          bottom: BorderSide(color: Colors.green, width: 2)),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Sixth small box with multiple borders
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                        bottom: BorderSide(color: Colors.green, width: 2),
                        right: BorderSide(color: Colors.red, width: 4),
                      ),
                    ),
                  ),
                  SizedBox(height: 20), // Space between small boxes
                  // Seventh small box with multiple borders
                  Container(
                    width: 50,
                    height: 25,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border(
                        bottom: BorderSide(color: Colors.orange, width: 10),
                        right: BorderSide(color: Colors.green, width: 2),
                        top: BorderSide(color: Colors.blue, width: 4),
                        left: BorderSide(color: Colors.green, width: 2),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
