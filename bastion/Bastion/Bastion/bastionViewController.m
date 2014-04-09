//
//  bastionViewController.m
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "bastionViewController.h"
#import "Communicator.h"
#import "UserAction.h"

@interface bastionViewController ()
@property (nonatomic, strong) Communicator *com;
@property (nonatomic, strong) UserAction *uact;
@end

@implementation bastionViewController

@synthesize webView = _webView;
@synthesize urlInput = _urlInput;
@synthesize com = _com;
@synthesize uact = _uact;

//@synthesize backButton = _backButton;
//@synthesize forwardButton = _forwardButton;
//@synthesize refreshButton = _refreshButton;

- (Communicator *)com
{
    if (!_com) _com = [[Communicator alloc] init];
    return _com;
}

- (UserAction *) uact
{
    if (!_uact) _uact = [[UserAction alloc] init];
    return _uact;
}

- (IBAction)goToSite
{
    NSLog(@"Go button hit");
    NSURLRequest *request = [self.com sendWebRequest:_urlInput.text];
    [_webView loadRequest:request];
}

- (IBAction)backAction
{
    NSLog(@"Back button hit");
    NSURLRequest *request = [self.com sendAction:@"back"];
    [_webView loadRequest:request];
}

- (IBAction)forwardAction
{
    NSLog(@"Forward button hit");
}

- (IBAction)refreshAction
{
    NSLog(@"Refresh button hit");
}

- (IBAction)favoritesMenuAction{
    NSLog(@"Favorites button hit");
}


- (void)webViewDidStartLoad:(UIWebView *)webView
{
    [UIApplication sharedApplication].networkActivityIndicatorVisible = YES;
}

- (void)webViewDidFinishLoad:(UIWebView *)webView
{
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
}

- (void)webView:(UIWebView *)webView didFailLoadWithError:(NSError *)error
{
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
    
    NSString *errorString = [error localizedDescription];
    [[UIAlertView alloc] initWithTitle:[NSString stringWithFormat:@"Error (%ld)", (long)error.code] message:errorString delegate:self cancelButtonTitle:nil otherButtonTitles:@"OK", nil];
    
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
