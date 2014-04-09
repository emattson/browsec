//
//  bastionViewController.h
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface bastionViewController : UIViewController <UIWebViewDelegate, UIAlertViewDelegate>
@property (weak, nonatomic) IBOutlet UITextField *urlInput;
@property (weak, nonatomic) IBOutlet UIWebView *webView;

@end
