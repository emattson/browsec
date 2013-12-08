//
//  pictureviewerViewController.h
//  PictureViewer
//
//  Created by Eli Mattson on 10/12/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface pictureviewerViewController : UIViewController

@property (weak, nonatomic) IBOutlet UIWebView *myWebView;
@property (weak, nonatomic) IBOutlet UITextField *urlInput;

@end
