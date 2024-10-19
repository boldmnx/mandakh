import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Лаб 8',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
        ),
        body: Center(
            child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            RichText(
              text: const TextSpan(children: [
                TextSpan(
                  text: 'Мэдээллийн ',
                  style: TextStyle(fontSize: 12),
                ),
                TextSpan(
                  text: 'систем\n',
                  style: TextStyle(
                      color: Colors.red,
                      fontSize: 12,
                      fontWeight: FontWeight.bold),
                ),
                TextSpan(
                    text: 'Программ ',
                    style: TextStyle(
                        fontStyle: FontStyle.italic,
                        fontSize: 12,
                        color: Colors.blue)),
                TextSpan(
                  text: 'хангамж\n', // Fourth part with different color
                  style: TextStyle(),
                ),
                TextSpan(text: '      Мандах Их Сургууль '),
                TextSpan(
                    text: 'Мэдээлэл, ',
                    style: TextStyle(decoration: TextDecoration.lineThrough)),
                TextSpan(text: 'Технологийн Сургууль \n', style: TextStyle()),
              ]),
            ),
            Container(
              width: 300,
              child: RichText(
                  textAlign: TextAlign.right,
                  text: const TextSpan(
                      style: TextStyle(
                          color: Colors.yellow,
                          fontSize: 11,
                          backgroundColor: Colors.black),
                      children: [
                        TextSpan(
                            text:
                                'Чанарын удирдлагын олон улсын стандарт ISO 9001 2012 болон Болорсролын байгууллагын '),
                        TextSpan(
                            text: 'менежментийн тогтолцооны ISO 21001:2018 ',
                            style: TextStyle(fontWeight: FontWeight.bold)),
                        TextSpan(
                            text:
                                'олон улсын стандартуудыг  нэвтрүүлсэн анхны их сургууль.')
                      ])),
            ),
            Container(
                width: 380,
                child: RichText(
                    textAlign: TextAlign.center,
                    text: const TextSpan(
                        style: TextStyle(decoration: TextDecoration.underline),
                        children: [
                          TextSpan(
                              text: 'Чанартай сургалт ',
                              style: TextStyle(fontSize: 18)),
                          TextSpan(
                              text: 'Чадтарлага мэргэжилтэн ',
                              style: TextStyle(
                                  color: Colors.red,
                                  fontWeight: FontWeight.bold,
                                  fontSize: 18)),
                          TextSpan(
                              text: 'Ёс зүй, хариуцлага Оюунлаг',
                              style: TextStyle(fontSize: 18)),
                          TextSpan(
                              text: ', хүнлэг,',
                              style: TextStyle(
                                  backgroundColor: Colors.purple,
                                  fontSize: 18,
                                  fontWeight: FontWeight.bold,
                                  fontStyle: FontStyle.italic)),
                          TextSpan(
                              text: ' нэгдмэл ',
                              style: TextStyle(fontSize: 18)),
                          TextSpan(
                              text: 'байдал',
                              style: TextStyle(
                                  backgroundColor: Colors.purple,
                                  fontSize: 18,
                                  fontWeight: FontWeight.bold,
                                  fontStyle: FontStyle.italic)),
                        ])))
          ],
        )),
      ),
    );
  }
}
