import 'package:flutter/material.dart';
import 'package:transparent_image/transparent_image.dart';
import 'package:video_player/video_player.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Assets & media',
      theme: ThemeData(
        // This is the theme of your application.
        //
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Assets & media'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late VideoPlayerController _controller;
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.network(
        'https://www.rmp-streaming.com/media/big-buck-bunny-360p.mp4') // Change to your video path
      ..initialize().then((_) {
        setState(() {});
      });
  }

  @override
  void dispose() {
    super.dispose();
    _controller.dispose();
  }

  void _togglePlayPause() {
    setState(() {
      if (_isPlaying) {
        _controller.pause();
      } else {
        _controller.play();
      }
      _isPlaying = !_isPlaying;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Asset Demo')),
      body: Center(
          child: Container(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          mainAxisSize: MainAxisSize.max,
          children: [
            SizedBox(width: 20),
            Expanded(
              child: Column(
                children: [
                  Image.asset('assets/images/cat.jpg', height: 200),
                  SizedBox(
                    width: 50,
                  ),
                  _controller.value.isInitialized
                      ? Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            AspectRatio(
                              aspectRatio: _controller.value.aspectRatio,
                              child: VideoPlayer(_controller),
                            ),
                            IconButton(
                              icon: Icon(
                                _isPlaying ? Icons.pause : Icons.play_arrow,
                                size: 50,
                              ),
                              onPressed: _togglePlayPause,
                            ),
                          ],
                        )
                      : CircularProgressIndicator(),
                ],
              ),
            ),
            Expanded(
              child: Column(
                children: [
                  Image.network('https://picsum.photos/250?image=9'),
                  SizedBox(width: 20),
                  FadeInImage.memoryNetwork(
                    placeholder: kTransparentImage,
                    image:
                        'https://images.pexels.com/photos/29357132/pexels-photo-29357132/free-photo-of-calm-dog-relaxing-on-green-grass-outdoors.jpeg',
                  ),
                ],
              ),
            ),
          ],
        ),
      )),
    );
  }
}
