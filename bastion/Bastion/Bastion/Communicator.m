//
//  Communicator.m
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "Communicator.h"

@implementation Communicator

-(NSURLRequest *) sendWebRequest: (NSString *) address {
    NSLog(@"made it this far");
    NSLog(@"Address requested is: %@", address);
    
    NSString *fullURL = @"http://www.google.com";
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *req = [NSURLRequest requestWithURL:url];
    
    return req;
}

-(NSObject *) getWebsite {
    //get website picture/image and pass it on
    return nil;
}

-(NSObject *) getActionFramework {
    //get action framework (hashtable structure)
    return nil;
}

-(void) sendAction:(NSObject *)userAction {
    //send user action back to
}

@end