//
//  HelloWorldAppDelegate.h
//  HelloWorld1
//
//  Created by Eli Mattson on 9/18/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import <UIKit/UIKit.h>

@class HelloWorldViewController;

@interface HelloWorldAppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@property (strong, nonatomic) HelloWorldViewController *viewController;

@end
