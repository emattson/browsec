//
//  HelloWorldViewController.m
//  HelloWorld1
//
//  Created by Eli Mattson on 9/18/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "HelloWorldViewController.h"

@interface HelloWorldViewController ()

@end

@implementation HelloWorldViewController

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

- (IBAction)showMessage{
    UIAlertView *helloworldAlert =  [[UIAlertView alloc] initWithTitle:@"My first hw" message:@"Hello World! Lets kick it" delegate:nil cancelButtonTitle:@"Done" otherButtonTitles:nil];
    
    [helloworldAlert show];
}

@end
