//
//  bastionViewController.m
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "bastionViewController.h"
#import "Communicator.h"

@interface bastionViewController ()
@property (nonatomic, strong) Communicator *com;
@end

@implementation bastionViewController

@synthesize webView = _webView;
@synthesize urlInput = _urlInput;
@synthesize com = _com;

- (Communicator *)com
{
    if (!_com) _com = [[Communicator alloc] init];
    return _com;
}

- (IBAction)goToSite
{
    NSLog(@"Go button hit");
    NSURLRequest *request = [self.com sendWebRequest:_urlInput.text];
    [_webView loadRequest:request];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
