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

- (IBAction)loadImage {
    NSString *fullURL = @"http://elisd.files.wordpress.com/2013/10/wiki_sec.png";
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    
    [_myWebView loadRequest:request];
}


@end
