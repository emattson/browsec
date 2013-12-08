//
//  pictureviewerViewController.m
//  PictureViewer
//
//  Created by Eli Mattson on 10/12/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "pictureviewerViewController.h"

@interface pictureviewerViewController ()

@end

@implementation pictureviewerViewController

@synthesize myWebView = _myWebView;
@synthesize urlInput = _urlInput;



- (IBAction)loadImage {
    NSLog(@"loadImage selected, url is %@", _urlInput.text);
    NSString *fullURL = @"http://10.0.2.15:8000/Desktop/google.png";
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    
    [_myWebView loadRequest:request];
}


@end
