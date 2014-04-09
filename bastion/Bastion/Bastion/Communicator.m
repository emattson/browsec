//
//  Communicator.m
//  Bastion
//
//  Created by Eli Mattson on 10/26/13.
//  Copyright (c) 2013 Eli Mattson. All rights reserved.
//

#import "Communicator.h"
#import "NSData+Base64.h"

@implementation Communicator

#define base @"http://nimbus.seas.gwu.edu:8888/src/"
//@"http://54.201.101.85:8080/"

-(NSURLRequest *) sendWebRequest: (NSString *) address {
//    NSLog(@"made it this far");
    NSLog(@"Address requested is: %@", address);
    NSData *data = [address dataUsingEncoding:NSASCIIStringEncoding];
    NSString *encodedURL = [data base64EncodedString];
    NSLog(@"encoded string is: %@", encodedURL);
    NSString *fullURL = base;
    fullURL = [fullURL stringByAppendingString:encodedURL];
    NSLog(@"fullUrl is %@", fullURL);
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

-(NSURLRequest *) sendAction:(NSString *)userAction {
    //send user action back to
    NSLog(@"action is %@", userAction);
    NSString *fullURL = @"http://nimbus.seas.gwu.edu:8888/_";
    fullURL = [fullURL stringByAppendingString:userAction];
    NSLog(@"full url is %@", fullURL);
    NSURL *url = [NSURL URLWithString:fullURL];
    NSURLRequest *req = [NSURLRequest requestWithURL:url];
    return req;
}

@end